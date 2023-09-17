"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#read-only-and-write-only-fields"""

from pprint import pprint
import datetime as dt

from marshmallow import Schema, fields, INCLUDE


class UserSchema(Schema):
    name = fields.Str()
    # password is "write-only"
    password = fields.Str(load_only=True)
    # created_at is "read-only"
    created_at = fields.DateTime(dump_only=True)


pprint(UserSchema().dump({"password": 'qwerty', "created_at": dt.datetime.now()}))
pprint(UserSchema().load({"password": 'qwerty', "created_at": dt.datetime.now()}, unknown=INCLUDE))
