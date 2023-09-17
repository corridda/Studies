"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#filtering-output"""

from pprint import pprint

from utl import *

user = User(name="Monty", email="monty@python.org")
summary_schema = UserSchema(only=("name", "email"))
result = summary_schema.dump(user)
pprint(result)
