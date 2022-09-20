from typing import List

from fastapi import APIRouter

from db import schemas
from db.user import session_add_new_user, session_get_users, session_get_user_by_id
from helpers.db_session import get_session

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.post("")
def create_user(
    user: schemas.User,
) -> schemas.User:
    inner_session = get_session(connection_type="readwrite")
    
    new_user = session_add_new_user(
        outer_session=inner_session,
        name=user.name,
        email=user.email    
    )

    inner_session.close()

    return new_user


@router.get("")
def get_users() -> List[schemas.User]:
    inner_session = get_session(connection_type="readwrite")

    users_generator = session_get_users(
        outer_session=inner_session
    )
    users = list(users_generator)

    inner_session.close()

    return users


@router.get("/{user_id}", response_model=schemas.User)
def get_user_by_id(
    user_id: str,
) -> schemas.User:
    inner_session = get_session(connection_type="readwrite")

    user = session_get_user_by_id(
        outer_session=inner_session,
        user_id=user_id
    )

    inner_session.close()

    return user
