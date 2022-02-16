import os
import sys
import unittest

import keyvaluedb

# TODO: Add more tests for dictionary and tests for server


class TestClass(unittest.TestCase):
    def setUp(self):
        location = os.path.join(sys.path[0], "example.data")
        self.db = keyvaluedb.load(location)

    def test_lookup(self):
        test_key = "3f47dc34-c2e9-4f00-98f1-337d16423934"
        result = self.db.get(str.encode(test_key))
        self.assertEqual(result, b"zyalpvvu")


if __name__ == "__main__":
    unittest.main()
