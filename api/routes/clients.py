from typing import List

from fastapi import APIRouter

from db import schemas
from db.client import session_add_new_client, session_get_clients, session_get_client_by_email
from helpers.db_session import get_session

router = APIRouter(
    prefix="/clients",
    tags=["Client"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=schemas.Client)
def create_client(
    client: schemas.Client,
) -> schemas.Client:
    inner_session = get_session(connection_type="readwrite")
    
    new_client = session_add_new_client(
        outer_session=inner_session,
        user_id=client.user_id,
        phone_number=client.phone_number,
    )

    inner_session.close()

    return new_client


@router.get("", response_model=List[schemas.Client])
def get_clients() -> List[schemas.Client]:
    inner_session = get_session(connection_type="readwrite")

    clients_generator = session_get_clients(
        outer_session=inner_session
    )
    clients = list(clients_generator)

    inner_session.close()

    return clients


@router.get("/{email}")
def get_client_by_id(
    email: str,
) -> schemas.Client:
    inner_session = get_session(connection_type="readwrite")

    res = session_get_client_by_email(
        outer_session=inner_session,
        email=email
    )

    inner_session.close()
    user = res[0].as_dict()
    client = res[1].as_dict()

    return {
        "user": user,
        "client": client
    }
