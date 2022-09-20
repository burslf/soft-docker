import json

from helpers.custom_log import get_logger
from helpers.db_session import get_session
from helpers.decorators.api_gateway_handler import api_gateway_handler
from helpers.utils import get_body_from_event

logger = get_logger()


@api_gateway_handler
def api_book_delivery(event: {}, context: {}):
    body = get_body_from_event(event=event)

    user = body.get("user")
    timeslot_id = body.get("timeslot_id")

    conditional_fields = ["user", "timeslot_id"]

    if None in [user, timeslot_id]:
        raise Exception(f"Missing required field: {conditional_fields}")

    # Open courier static json file
    courier_api_file = open('utils/courier_api.json')
    courier_timeslots = json.load(courier_api_file)

    if not courier_timeslots[timeslot_id]:
        raise Exception(f"Timeslot not found for this id")

    session = get_session()

    user_in_db = get_user_by_name(session=session, name=user["name"])

    if not user_in_db:
        raise Exception(f"User not found for this name")

    new_delivery = add_new_delivery(session=session, timeslot_id=timeslot_id, user_id=user_in_db["_id"])

    return new_delivery
