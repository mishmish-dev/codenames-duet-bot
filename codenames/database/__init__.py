from sqlalchemy import create_engine

from codenames.database.session import session_factory, create_session_context
from codenames.database.models import BaseModel


def initialize(connection_string: str, echo_sql: bool = False) -> None:
    engine = create_engine(connection_string, echo=echo_sql)
    session_factory.configure(bind=engine)

    BaseModel.metadata.create_all(engine)
