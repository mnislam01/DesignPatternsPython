import copy


class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


john = Person('John', Address('123 London Road', 'London', 'UK'))
print(john)
jane = copy.deepcopy(john)
jane.name = 'Jane'
print('----')
print(jane)
print(john)
jane.address.street = '123B London Road'
print('Jane Moved')
print(jane)
print('John still lives')
print(john)

