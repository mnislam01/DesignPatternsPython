from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is good')

class Coffee(HotDrink):
    def consume(self):
        print('This coffee is good')

class HotDrinkFactory(ABC):
    def prepare(self):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in the tea bag, hot water, suger, pour {amount}ml, serve!')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind coffee beans, put hot water, suger, pour {amount}ml, serve!')
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            for d in self.AvailableDrink:
                name = d.name.title()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Avilable drinks: ')
        for f in self.factories:
            print(f[0])

        idx = int(input(f'Pick (0-{len(self.factories)-1}): '))
        amount = int(input(f'Specify amount: '))
        return self.factories[idx][1].prepare(amount)



if __name__ == "__main__":
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
