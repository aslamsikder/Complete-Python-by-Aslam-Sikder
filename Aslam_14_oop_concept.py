# Object oriented programming

class Employee:
    #   Double UnderScore ( _ _ ) means  private variable
    __name = None
    __id = 0
    __salary = 0

    # Creating Constructor
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    #   Creating get() & set() method for accessing the private variables
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_salary(self, salary):
        self.__id = salary

    def get_salary(self):
        return self.__salary

#   Creating an object of Employee class
aslam = Employee('Aslam Sikder', 143, 120000)

print(aslam.get_name())
print(aslam.get_id())
print(aslam.get_salary())

