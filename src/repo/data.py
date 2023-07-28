from typing import List

from sqlalchemy.orm import Session

from src.db.model.data import Data

from src.db.database import Database

from src.core.config import get_config

config = get_config()


class DataRepo:

    def __init__(self, session: Session):
        self.session = session
        self.table = config.etl_table

    def get_all(self) -> List[Data]:
        rows = self.session.execute(f"select * from {self.table}")
        columns = Database.get_columns(self.session, self.table)
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
