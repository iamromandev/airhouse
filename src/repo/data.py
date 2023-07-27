from typing import List

from sqlalchemy.orm import Session

from src.db.model.data import Data


class DataRepo:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Data]:
        result = self.session.execute("SELECT * FROM local")

        for row in result:
            print(row)
        return Data()
