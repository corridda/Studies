"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#validation-without-deserialization"""

from utl import *

errors = UserSchema().validate({"name": "Ronnie", "email": "invalid-email"})
print(errors)  # {'email': ['Not a valid email address.']}
