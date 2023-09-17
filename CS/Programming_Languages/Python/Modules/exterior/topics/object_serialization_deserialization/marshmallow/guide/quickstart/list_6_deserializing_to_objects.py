"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#deserializing-to-objects"""

from marshmallow import Schema, fields, post_load

from utl import User

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

if __name__ == '__main__':
    user_data = {"name": "Ronnie", "email": "ronnie@stones.com"}
    schema = UserSchema()
    result = schema.load(user_data)
    print(result)  # => <User(name='Ronnie')