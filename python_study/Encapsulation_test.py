class Student:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number


student = Student("민지", 13)
print(student.get_name())
print(student.get_number())


class Student:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, _name):
        self.__name = _name

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, _number):
        self.__number = _number


student = Student("민지", 13)
# print(student.name())
# print(student.number())
print(student.name)
print(student.number)
