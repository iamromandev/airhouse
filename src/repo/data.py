from typing import List

from sqlalchemy.orm import Session

from src.db.model.data import Data

from src.db.database import Database


class DataRepo:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Data]:
        rows = self.session.execute("SELECT * FROM local")
        columns = Database.get_columns(self.session, "local")
        print(columns)

        data = [
            Data(
                date=row[columns["date"]],
                key=row[columns["key"]],
            )
            for row in rows
        ]

        return data
