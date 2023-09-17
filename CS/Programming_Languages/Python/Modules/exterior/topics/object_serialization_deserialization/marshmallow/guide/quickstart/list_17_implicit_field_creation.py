"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#implicit-field-creation"""

from marshmallow import Schema, fields


class UserSchema(Schema):
    uppername = fields.Function(lambda obj: obj.name.upper())

    class Meta:
        fields = ("name", "email", "created_at", "uppername")


class UserSchema_var2(Schema):
    uppername = fields.Function(lambda obj: obj.name.upper())

    class Meta:
        # No need to include 'uppername'
        additional = ("name", "email", "created_at")
