"""https://marshmallow.readthedocs.io/en/stable/quickstart.html
#specifying-defaults"""

import datetime as dt
import uuid
from pprint import pprint

from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.UUID(load_default=uuid.uuid1)
    birthdate = fields.DateTime(dump_default=dt.datetime(2017, 9, 29))


result_1 = UserSchema().load({})
pprint(result_1)
# {'id': UUID('337d946c-32cd-11e8-b475-0022192ed31b')}

result_2 = UserSchema().dump({})
pprint(result_2)
# {'birthdate': '2017-09-29T00:00:00+00:00'}
