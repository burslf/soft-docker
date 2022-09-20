import json

from api_endpoints.get_client_by_email import get_client_by_email
from db.client import session_get_client_by_email, session_add_new_client
from db.user import session_add_new_user

from helpers.db_session import get_session
from helpers.load_env import load_environment_variables

load_environment_variables(env="develop", parent_level=0)

# event = {
#     "body":  json.dumps({"user": {
#             "name": "eden",
#             "email": "eden@gmail.com",
#             "phone_number": "0111111111"
#         }})
# }

session = get_session(connection_type="readwrite")

res = session_add_new_user(outer_session=session, name="yoel", email="yoelzerbib7@gmail.com")

# res = create_new_client(event=event, context={})
# res = session_get_users(outer_session=session)
# res = session_get_clients(outer_session=session)
# res = get_client_by_email(event={"body": json.dumps({"email": "yoelzerbib7@gmail.com"})}, context={})
# user, client = session_get_client_by_email(outer_session=session, email="yoelzerbib7@gmail.com")
print(res)
