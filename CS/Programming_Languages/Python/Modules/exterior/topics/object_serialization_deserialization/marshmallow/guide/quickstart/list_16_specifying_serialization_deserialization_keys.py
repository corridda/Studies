"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#specifying-serialization-deserialization-keys"""

from pprint import pprint

from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email(data_key="emailAddress")


s = UserSchema()

data = {"name": "Mike", "email": "foo@bar.com"}
result = s.dump(data)
pprint(result)
# {'name': u'Mike',
# 'emailAddress': 'foo@bar.com'}

data = {"name": "Mike", "emailAddress": "foo@bar.com"}
result_1 = s.load(data)
pprint(result_1)
# {'name': u'Mike',
# 'email': 'foo@bar.com'}
