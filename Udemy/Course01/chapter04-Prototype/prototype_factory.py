import copy


class Address:
    def __init__(self, street, suit, country):
        self.street = street
        self.suit = suit
        self.country = country

    def __str__(self):
        return f'{self.street}, # {self.suit}, {self.country}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123 East Dr', 0, 'London'))
    aux_office_employee = Employee('', Address('123B East Dr', 0, 'London'))

    @staticmethod
    def __new_employee(proto, name, suit):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suit = suit
        return result 

    @staticmethod
    def new_main_office_employee(name, suit):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, 
            name, suit
        )

    @staticmethod
    def new_aux_office_employee(name, suit):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suit
        )



john = EmployeeFactory.new_main_office_employee('John', 101)
jane = EmployeeFactory.new_aux_office_employee('Jane', 101)
print(john, '\n', jane)
