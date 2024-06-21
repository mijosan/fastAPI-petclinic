from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy.orm import Session, joinedload

from auth.utils import create_access_token, get_password_hash, verify_password
from role.models import RoleModel
from user.exceptions import (InvalidCredentialsException,
                             UserEmailAlreadyExistsException,
                             UserIdAlreadyExistsException,
                             UserNotFoundException)

from .models import UserModel
from .schemas import UserRequest, UserResponse, UserSchema


class UserService:
    def __init__(self, db: Session):
        self.db = db
        
    def create_user(self, user_request: UserRequest) -> UserResponse:
        try:
            with self.db.begin():
                # id 중복 체크
                stmt = select(UserModel).where(UserModel.id == user_request.id)
                existing_user = self.db.execute(stmt).scalar_one_or_none()
                if existing_user:
                    raise UserIdAlreadyExistsException(user_request.id)

                # email 중복 체크
                stmt = select(UserModel).where(UserModel.email == user_request.email)
                existing_email = self.db.execute(stmt).scalar_one_or_none()
                if existing_email:
                    raise UserEmailAlreadyExistsException(user_request.email)
                
                default_role = self.db.execute(select(RoleModel).where(RoleModel.id == 2)).scalar_one_or_none()
                
                user_model = UserModel(
                    id = user_request.id,
                    email = user_request.email,
                    password = get_password_hash(user_request.password),
                )
                
                self.db.add(user_model)
    
                # 기본 역할 추가
                user_model.roles.append(default_role)
                
                user_list = []
                user_list.append(UserSchema.from_orm(user_model))
                
                self.db.commit()

                return UserResponse(message="User created successfully", users=user_list)
        except SQLAlchemyError:
            self.db.rollback()
            
            raise Exception
        
    def login_user(self, OAuth2_password_request_form: OAuth2PasswordRequestForm):
        user = self.db.query(UserModel).options(joinedload(UserModel.roles)).filter(UserModel.id == OAuth2_password_request_form.username).first()
        
        if not user or not verify_password(OAuth2_password_request_form.password, user.password):
            raise InvalidCredentialsException()

        user_schema = UserSchema.model_validate(user)

        # roles를 dictionary로 변환
        roles_as_dict = [role.model_dump() for role in user_schema.roles]
        user_data = user_schema.model_dump()
        user_data['roles'] = roles_as_dict

        access_token = create_access_token(data={"id": user_data['id'], "roles": user_data['roles']})
        
        return access_token
    
    def get_users(self, user_request: UserRequest) -> UserResponse:
        stmt = select(UserModel)
        
        # 조건부 필터링
        if user_request.id:
            stmt = stmt.where(UserModel.id.like(f"%{user_request.id}%"))
        
        # 페이지네이션 적용
        stmt = stmt.offset(user_request.skip).limit(user_request.limit)
        
        users = self.db.execute(stmt).scalars().all()
        
        # SQLAlchemy 객체를 Pydantic 객체로 변환
        user_list = [UserSchema.model_validate(user) for user in users]

        return UserResponse(users = user_list)

    def get_user(self, id: str) -> UserResponse:
        stmt = select(UserModel).where(UserModel.id == id)
        
        user = self.db.execute(stmt).scalar_one_or_none()
        
        if user is None:
            raise UserNotFoundException(id)

        user_schema = [UserSchema.model_validate(user)]

        return UserResponse(users = user_schema)