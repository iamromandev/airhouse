from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field


class DataBase(SQLModel):
    date: str = Field()
    key: Optional[str] = Field(default=None)
    new_confirmed: Optional[int] = Field(default=None)
    new_deceased: Optional[int] = Field(default=None)
    new_recovered: Optional[int] = Field(default=None)
    new_tested: Optional[int] = Field(default=None)
    total_confirmed: Optional[int] = Field(default=None)
    total_deceased: Optional[int] = Field(default=None)
    total_recovered: Optional[int] = Field(default=None)
    total_tested: Optional[int] = Field(default=None)


class Data(DataBase, table=False):
    pass


class DataRead(DataBase):
    pass
