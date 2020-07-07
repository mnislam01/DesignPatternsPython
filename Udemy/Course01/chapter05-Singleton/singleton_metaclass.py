import unittest

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading Database')

class TestSingleton(unittest.TestCase):

    def test_singleton_database_instance(self):
        d1 = Database()
        d2 = Database()
        self.assertEqual(d1,d1)

if __name__ == "__main__":
    unittest.main()

