from typing import Type, TypeVar, Generator, Any, Dict

# from sqlmodel import (
#     create_engine,
#     SQLModel,
#     Session,
#     select,
# )
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session

from src.core.config import get_config, Env

config = get_config()
print(config.db_url)
engine = create_engine(config.db_url)


# Session = sessionmaker(bind=engine)

# Session = sessionmaker(bind=engine)

# T = TypeVar("T", bound=SQLModel)


class Database:

    # @classmethod
    # def get_session(cls) -> Generator[Session, None, None]:
    #     with Session(engine) as session:
    #         yield session

    @classmethod
    def get_session(cls) -> Generator[Session, None, None]:
        with Session(bind=engine) as session:
            yield session

    @classmethod
    def get_columns(cls, session: Session, table: str) -> Dict[str, int]:
        query = f"SELECT column_name, ordinal_position FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{table}'"
        rows = session.execute(query)

        columns = {
            row[0]: (row[1] - 1)
            for row in rows
        }

        return columns

    # @classmethod
    # def update_sql_model(cls, model: T, updates: T) -> None:
    #     update_data = updates.dict(exclude_unset=True)
    #     for key, value in update_data.items():
    #         setattr(model, key, value)

    # @classmethod
    # def get_by_prop(
    #     cls,
    #     session: Session,
    #     model: Type[T],
    #     prop: str,
    #     value: Any
    # ) -> T:
    #     prop = getattr(model, prop)
    #     return session.exec(select(model).where(prop == value)).first()

    @classmethod
    def init_db(cls):
        # SQLModel.metadata.create_all(engine)
        pass

    @classmethod
    def create_db_and_tables(cls):
        # SQLModel.metadata.create_all(engine)
        pass
