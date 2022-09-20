import json
from typing import Dict

from db.client import session_add_new_client
from db.user import session_add_new_user
from helpers.custom_log import get_logger
from helpers.db_session import get_session
from helpers.decorators.api_gateway_handler import api_gateway_handler
from helpers.utils import get_body_from_event

logger = get_logger()


@api_gateway_handler
def create_new_client(event: Dict, context: Dict):
    body = get_body_from_event(event=event)

    user = body.get("user")
    conditional_fields = ["user"]

    if None in [user]:
        raise Exception(f"Missing required field: {conditional_fields}")

    payment_method = user.get("payment_method", False)
    phone_number = user.get("phone_number")
    name = user.get("name")
    email = user.get("email")

    conditional_values = ["name", "email", "phone_number"]

    if None in [name, email, phone_number]:
        raise Exception(f"Missing required field: {conditional_values}")

    session = get_session(connection_type="readwrite")

    new_user = session_add_new_user(outer_session=session, name=name, email=email)
    new_client = session_add_new_client(outer_session=session, user_id=new_user.id,
                                        phone_number=phone_number, payment_method=payment_method)

    return {
        "user": new_user.as_dict(),
        "client": new_client.as_dict()
    }
