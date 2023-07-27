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
                new_confirmed=row[columns["new_confirmed"]],
                new_deceased=row[columns["new_deceased"]],
                new_recovered=row[columns["new_recovered"]],
                new_tested=row[columns["new_tested"]],
                total_confirmed=row[columns["total_confirmed"]],
                total_deceased=row[columns["total_deceased"]],
                total_recovered=row[columns["total_recovered"]],
                total_tested=row[columns["total_tested"]]
            )
            for row in rows
        ]

        return data
