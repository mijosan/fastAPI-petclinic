
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from .exceptions import OwnerNotFoundException
from .models import Owner
from .schemas import OwnerRequest, OwnerResponse, Owner as SchemaOwner

class OwnerService:
    def __init__(self, db: Session):
        self.db = db

    def get_owners(self, owner_request: OwnerRequest) -> List[OwnerResponse]:
        try: 
            with self.db.begin(): 
                stmt = select(Owner)
                
                # 조건부 필터링
                if owner_request.name:
                    stmt = stmt.where(Owner.name.like(f"%{owner_request.name}%"))
                
                # 페이지네이션 적용
                stmt = stmt.offset(owner_request.skip).limit(owner_request.limit)
                
                owners = self.db.execute(stmt).scalars().all()
                
                # SQLAlchemy 객체를 Pydantic 객체로 변환
                owner_list = [SchemaOwner.from_orm(owner) for owner in owners]
        
                return OwnerResponse(owners=owner_list)
        except SQLAlchemyError:
            self.db.rollback()
            
            raise Exception
            
    def get_owner(self, owner_id: int) -> OwnerResponse:
        try: 
            with self.db.begin(): 
                stmt = select(Owner).where(Owner.id == owner_id)
                
                owner = self.db.execute(stmt).scalar_one_or_none()
                
                if owner is None:
                    raise OwnerNotFoundException(owner_id)

                owner_list = [owner]

                return OwnerResponse(owners=owner_list)
        except SQLAlchemyError:
            self.db.rollback()
            
            raise Exception
