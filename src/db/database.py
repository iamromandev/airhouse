from typing import Type, TypeVar, Generator, Any

from sqlmodel import (
    create_engine,
    SQLModel,
    Session,
    select,
)

from src.core.config import get_config, Env

config = get_config()
engine = create_engine(
    config.db_url,
    echo=(config.env == Env.local.value),
)

T = TypeVar("T", bound=SQLModel)


class Database:

    @classmethod
    def get_session(cls) -> Generator[Session, None, None]:
        with Session(engine) as session:
            yield session

    @classmethod
    def update_sql_model(cls, model: T, updates: T) -> None:
        update_data = updates.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(model, key, value)

    @classmethod
    def get_by_prop(
        cls,
        session: Session,
        model: Type[T],
        prop: str,
        value: Any
    ) -> T:
        prop = getattr(model, prop)
        return session.exec(select(model).where(prop == value)).first()

    @classmethod
    def init_db(cls):
        SQLModel.metadata.create_all(engine)

    @classmethod
    def create_db_and_tables(cls):
        SQLModel.metadata.create_all(engine)
