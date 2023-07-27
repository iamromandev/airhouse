from datetime import datetime

from sqlmodel import SQLModel, Field


class DataBase(SQLModel):
    date: datetime = Field()
    key: str = Field()


class Data(DataBase, table=False):
    pass


class DataRead(DataBase):
    pass
