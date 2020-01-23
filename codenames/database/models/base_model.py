from typing import Optional, Type, TypeVar

from sqlalchemy import Column, SmallInteger
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Session

from codenames.utils import to_snake_case_and_plural

from codenames.database.models.column_array import ColumnArray
from codenames.database.session import create_session_context


M = TypeVar("M", bound="BaseModel")

@as_declarative()
class BaseModel:
    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        arrays = [attr for attr in cls.__dict__.values() if isinstance(attr, ColumnArray)]
        for array in arrays:
            for index in range(array.max_length):
                setattr(cls, array.elem_column_template.format(index), Column(array.column_type))
            setattr(cls, array.len_column_name, Column(SmallInteger, nullable=False, default=0))

    @declared_attr
    def __tablename__(cls):
        return to_snake_case_and_plural(cls.__name__)

    @classmethod
    def get_or_create(cls: Type[M], id, session: Optional[Session] = None, **ctor_args) -> M:
        if session is None:
            with create_session_context() as session:
                instance = cls.get_or_create(id, session)
                session.expunge(instance)
                return instance

        instance = session.query(cls).get(id)
        if instance is None:
            instance = cls(id=id, **ctor_args)
            session.add(instance)

        return instance
