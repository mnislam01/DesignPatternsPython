import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.population = {}
        f = open("population.txt", "r")
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i+1].strip())

        f.close()


class SingletonRecordFinder(object):
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += DataBase().population[c]
        return result


class ConfigurableRecordFinder(object):
    def __init__(self, db=DataBase()):
        self.db = db
    
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result


class DummyDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name):
        return self.population[name]

class SingletonTests(unittest.TestCase):

    def test_is_singleton(self):
        db1 = DataBase()
        db2 = DataBase()

        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Manila', 'Seoul']
        tp = rf.total_population(names)
        self.assertEqual(232413432+23243432, tp)


    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(
            crf.total_population(['alpha', 'beta']),
            3
        )


if __name__ == "__main__":
    unittest.main()
