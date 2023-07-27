from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field


class DataBase(SQLModel):
    date: str = Field()
    key: Optional[str] = Field(default=None)


class Data(DataBase, table=False):
    pass


class DataRead(DataBase):
    pass
