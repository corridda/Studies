"""https://marshmallow.readthedocs.io/en/stable/quickstart.html#serializing-objects-dumping"""

from pprint import pprint
from utl import *

user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
print(f"type(result): {type(result)}")
pprint(result)

print()

# You can also serialize to a JSON-encoded string using dumps.
json_result = schema.dumps(user)
print(f"type(json_result): {type(json_result)}")
pprint(json_result)

