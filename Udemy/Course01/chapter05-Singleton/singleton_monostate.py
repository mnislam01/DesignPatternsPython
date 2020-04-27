class CEO:
    __shared_state = {
        'name': 'Steve',
        'age': 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Monostate:
    __shared_sate = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_sate
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_manage = 0
    
    def __str__(self):
        return f'{self.name} manages ${self.money_manage}'


if __name__ == "__main__":

    cfo1 = CFO()
    cfo1.name = 'Sheryl'
    cfo1.money_manage = 120

    # print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Nazrul'
    cfo2.money_manage = 50
    print(cfo1)
    print(cfo2)
    # ceo1 = CEO()
    # print(ceo1)

    # ceo2 = CEO()
    # ceo2.age = 77

    # print(ceo1)
    # print(ceo2)
    