"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#handling-collections-of-objects"""

from pprint import pprint

from utl import *

user1 = User(name="Mick", email="mick@stones.com")
user2 = User(name="Keith", email="keith@stones.com")
users = [user1, user2]
schema = UserSchema(many=True)
result = schema.dump(users)  # OR UserSchema().dump(users, many=True)
print(f"type(result): {type(result)}")
pprint(result)
