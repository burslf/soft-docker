from typing import List
from helpers.decorators.fname import fname
from helpers.custom_log import get_logger
from db.models import User
from db import schemas
from sqlalchemy.orm import Session

logger = get_logger()


@fname
def session_add_new_user(outer_session: Session, name: str, email: str):
    user = User()

    user.name = name
    user.email = email

    outer_session.add(user)
    outer_session.commit()

    return schemas.User.parse_obj(obj=user.as_dict())


@fname
def session_get_users(outer_session: Session) -> List[User]:
    conditional_fields = [outer_session]

    if None in conditional_fields:
        raise Exception(f"{fname} conditional_fields: {conditional_fields}")

    res: List[User] = outer_session.query(User).all()

    for user in res:
        yield schemas.User.parse_obj(obj=user.as_dict())

@fname
def session_get_user_by_id(outer_session: Session, user_id: int) -> User:
    conditional_fields = [outer_session]

    if None in conditional_fields:
        raise Exception(f"{fname} conditional_fields: {conditional_fields}")

    res: User = outer_session.query(User).filter(User.id == user_id).first()

    return schemas.User.parse_obj(obj=res.as_dict())