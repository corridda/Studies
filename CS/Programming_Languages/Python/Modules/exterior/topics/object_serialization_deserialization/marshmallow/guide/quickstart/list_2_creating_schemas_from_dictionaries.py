"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#creating-schemas-from-dictionaries"""

from marshmallow import Schema, fields

UserSchema = Schema.from_dict(
    {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
)

print(UserSchema)
