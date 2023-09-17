"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#handling-unknown-fields"""

"""
RAISE (default): raise a ValidationError if there are any unknown fields
EXCLUDE: exclude unknown fields
INCLUDE: accept and include the unknown fields
"""

from marshmallow import Schema, INCLUDE


class UserSchema(Schema):
    class Meta:
        unknown = INCLUDE

# OR
# schema = UserSchema(unknown=INCLUDE)

# OR
# UserSchema().load(data, unknown=INCLUDE)
