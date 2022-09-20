import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.pool import NullPool


def get_connection_string(connection_type: str):
    valid_connection_types = ["readonly", "readwrite"]

    if connection_type == "readonly":
        connection_string = os.getenv("DATABASE_RO_URL")
    elif connection_type == "readwrite":
        connection_string = os.getenv("DATABASE_URL")
    else:
        raise Exception(f"connection_type not in {valid_connection_types}")

    return connection_string


def get_session(connection_type: str) -> Session:
    connection_string = get_connection_string(connection_type=connection_type)

    # engine = create_engine(connection_string, poolclass=NullPool, pool_pre_ping=True)
    engine = create_engine(connection_string)

    session = sessionmaker(engine)

    return session()
