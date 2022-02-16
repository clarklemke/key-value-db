from typing import Union
import os


class KeyValueDB:
    def __init__(self, location: str) -> None:
        """Creates a database object and loads the data from the location path."""
        self.load(location)

    def load(self, location: str) -> bool:
        """Loads the data file"""
        location = os.path.expanduser(location)
        if os.path.exists(location):
            self._load_db(location)
        else:
            print("Data location does not exist")
            self.db = {}
        return True

    def _load_db(self, location: str) -> None:
        """Helper function to load data file"""
        self.db = {}
        with open(location) as f:
            for line in f:
                key, *values = line.split()
                self.db[str.encode(key)] = str.encode(" ".join(values))

    def get(self, key: str) -> Union[str, bool]:
        """Get the value of a key"""
        try:
            return self.db[key]
        except KeyError:
            return False

    def get_all(self) -> list:
        """Return a list of all keys in db"""
        return self.db.keys()

    def exists(self, key: str) -> bool:
        """Return True if key exists in db, return False if not"""
        return key in self.db

    def total_keys(self) -> int:
        """Get a total number of keys in db"""
        total = len(self.db)
        return total

    def del_db(self) -> bool:
        """Delete everything from the database"""
        self.db = {}
        return True


def load(location: str) -> KeyValueDB:
    """Return a database object and import data in location"""
    return KeyValueDB(location)
