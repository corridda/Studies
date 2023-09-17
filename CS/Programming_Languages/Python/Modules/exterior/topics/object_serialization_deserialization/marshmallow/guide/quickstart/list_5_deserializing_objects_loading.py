"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#deserializing-objects-loading"""

from pprint import pprint

from utl import *

user_data = {
    "created_at": "2014-08-11T05:26:03.869245",
    "email": "ken@yahoo.com",
    "name": "Ken",
    # "unexpected_field": "unexpected_value"
}

schema = UserSchema()
result = schema.load(user_data)
print(f"type(result): {type(result)}")
pprint(result)
