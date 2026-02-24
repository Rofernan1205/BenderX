from sqlalchemy.orm import Session
from app.models.branches import Branch
from typing import Optional

class BranchRepository:
    def __init__(self, db: Session):
        self._db = db

    def create(self, branch_data : dict) -> Branch :
        branch = Branch(**branch_data)
        self._db.add(branch)
        self._db.flush()
        return branch

    def update(self, branch_obj : Branch, clean_data: dict) -> Branch :
        for key, value in clean_data.items():
            if hasattr(branch_obj, key):
                setattr(branch_obj, key, value)
        self._db.flush()
        self._db.refresh(branch_obj)
        return branch_obj


    def get_by_id(self, id: int) -> Optional[Branch]:
        branch = self._db.query(Branch).filter(Branch.id == id).first()
        return branch

    def get_by_name(self, name: str) -> Optional[Branch]:
        branch = self._db.query(Branch).filter(Branch.name == name).first()
        return branch


    def delete(self, branch: Branch) -> None:
        self._db.delete(branch)
        self._db.flush()


    def get_all(self, page: int , limit: int) -> list[type[Branch]] :
        skip = (page - 1)* limit
        return self._db.query(Branch).offset(skip).limit(limit).all()




