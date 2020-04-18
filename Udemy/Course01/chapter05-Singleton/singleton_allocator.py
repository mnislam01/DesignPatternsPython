import random


class Database:
    _instance = None

    def __init__(self):
        a_id = random.randint(1, 100)
        print(f'Id: {a_id}')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)

