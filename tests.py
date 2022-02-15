import os
import sys

import keyvaluedb


class TestClass:

    location = os.path.join(sys.path[0], "example.data")
    db = keyvaluedb.load(location)

    print(db.get("3f47dc34-c2e9-4f00-98f1-337d16423934"))
    print(db.total_keys())

    # TODO: implement test cases
