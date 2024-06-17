from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from passlib.context import CryptContext

from user.exceptions import UserEmailAlreadyExistsException, UserIdAlreadyExistsException
from .models import UserModel
from .schemas import UserSchema, UserRequest, UserResponse

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

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
                
                user_model = UserModel(
                    id=user_request.id,
                    email=user_request.email,
                    password=self.get_password_hash(user_request.password)
                )
                
                self.db.add(user_model)
                
                user_list = []
                user_list.append(UserSchema.model_validate(user_model))
                
                self.db.commit()

                return UserResponse(message="User created successfully", users=user_list)
        except SQLAlchemyError:
            self.db.rollback()
            
            raise Exception