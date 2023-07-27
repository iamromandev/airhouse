from pydantic import BaseModel, BaseConfig

from src.core.util import to_camel


class Base(BaseModel):
    class Config(BaseConfig):
        alias_generator = to_camel
        allow_population_by_field_name = True
