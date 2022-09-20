from db.client import session_get_client_by_email
from helpers.custom_log import get_logger
from helpers.db_session import get_session
from helpers.decorators.api_gateway_handler import api_gateway_handler
from helpers.utils import get_body_from_event

logger = get_logger()


@api_gateway_handler
def get_client_by_email(event: {}, context: {}):
    body = get_body_from_event(event=event)

    email = body.get("email")

    conditional_fields = ["name", "email", "phone_number"]

    if None in [email]:
        raise Exception(f"Missing required field: {conditional_fields}")

    session = get_session(connection_type="readwrite")

    user, client = session_get_client_by_email(outer_session=session, email=email)

    return {
        "id": user.id,
        "name": user.name,
        "phone_number": client.phone_number,
        "payment_method": client.payment_method,
    }
