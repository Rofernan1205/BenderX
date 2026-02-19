from sqlalchemy.orm import Session

from app.models import Branch
from app.models.branches import Branch

class BranchRepository:
    def __init__(self, db: Session):
        self._db = db

    def create(self, branch_data : dict) -> Branch :
        branch = Branch(**branch_data)
        self._db.add(branch)
        self._db.flush()
        return branch

    def get_by_id(self, id: int) -> type[Branch] | None:
        branch = self._db.query(Branch).filter(Branch.id == id).first()
        return branch

    def get_by_name(self, name: str) -> type[Branch] | None:
        branch = self._db.query(Branch).filter(Branch.name == name).first()
        return branch

    def update(self, branch : Branch) -> Branch :
        self._db.flush()
        self._db.refresh(branch)
        return branch

    def delete(self, branch: Branch) -> None:
        self._db.delete(branch)
        self._db.flush()


    def get_all(self, page: int , limit: int) :
        skip = (page - 1)* limit
        return self._db.query(Branch).offset(skip).limit(limit).all()




