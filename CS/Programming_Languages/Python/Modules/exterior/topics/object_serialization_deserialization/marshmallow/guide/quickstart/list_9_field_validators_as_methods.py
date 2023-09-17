"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#field-validators-as-methods"""

from marshmallow import fields, Schema, validates, ValidationError


class ItemSchema(Schema):
    quantity = fields.Integer()

    @validates("quantity")
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError("Quantity must be greater than 0.")
        if value > 30:
            raise ValidationError("Quantity must not be greater than 30.")


if __name__ == '__main__':
    in_data = {"quantity": 31}
    try:
        result = ItemSchema().load(in_data)
    except ValidationError as err:
        print(err.messages)  # => {'quantity': ['Quantity must not be greater than 30.']}
