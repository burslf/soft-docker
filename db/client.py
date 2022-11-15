from typing import List, Tuple
from helpers.decorators.fname import fname
from helpers.custom_log import get_logger
from db.models import Client, User
from sqlalchemy.orm import Session, joinedload

logger = get_logger()


@fname
def session_add_new_client(outer_session: Session, user_id: str, phone_number: str, payment_method: bool = False):
    client = Client()

    client.user_id = user_id
    client.phone_number = phone_number
    client.payment_method = payment_method

    outer_session.add(client)
    outer_session.commit()

    return client


@fname
def session_get_clients(outer_session: Session) -> List[Client]:
    conditional_fields = [outer_session]

    if None in conditional_fields:
        raise Exception(f"{fname} conditional_fields: {conditional_fields}")

    res = outer_session.query(Client, User).filter(Client.user_id == User.id).all()

    return res


@fname
def session_get_client_by_email(outer_session: Session, email: str) -> Tuple[User, Client]:
    conditional_fields = [outer_session]

    if None in conditional_fields:
        raise Exception(f"{fname} conditional_fields: {conditional_fields}")

    res = outer_session.query(User, Client).join(Client).filter(User.email == email).first()
    user, client = res
    # user: User
    # client: Client

    return res
