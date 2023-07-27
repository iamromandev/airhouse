from typing import List

from sqlalchemy.orm import Session

from src.db.model.data import Data

from src.repo.data import DataRepo


class DataService:

    def __init__(self, session: Session):
        self.repo = DataRepo(session)

    def get_all(self) -> List[Data]:
        return self.repo.get_all()
