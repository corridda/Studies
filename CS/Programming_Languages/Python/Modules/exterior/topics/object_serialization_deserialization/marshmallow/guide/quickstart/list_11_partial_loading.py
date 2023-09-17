"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#partial-loading"""

from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)


result = UserSchema().load({"age": 42}, partial=("name",))
result_2 = UserSchema(partial=('name',)).load({'age': 42})
print(result)  # => {'age': 42}
print(result_2)  # => {'age': 42}

# You can ignore missing fields entirely by setting partial=True.
result_3 = UserSchema().load({}, partial=True)
result_4 = UserSchema(partial=True).load({'age': 42})
print(result_3)  # => {}
print(result_4)  # => {'age': 42}
