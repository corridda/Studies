"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#validation"""

from marshmallow import ValidationError

from utl import *

try:
    result = UserSchema().load({"name": "John", "email": "foo"})
except ValidationError as err:
    print(err.messages)  # => {"email": ['"foo" is not a valid email address.']}
    print(err.valid_data)  # => {"name": "John"}