"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#declaring-schemas"""

import datetime as dt


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return f"<User(name={self.name!r})>"

print(User("user_1", "e-mail_1"))
