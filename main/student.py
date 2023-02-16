class Student:

    def __init__(self, my_id, name,
                 sex, age, sc_math,
                 sc_physical, sc_chemistry):
        self._id = my_id
        self._name = name
        self._sex = sex
        self._age = age
        self._sc_math = sc_math
        self._sc_physical = sc_physical
        self._sc_chemistry = sc_chemistry
        self._sc_average = 0
        self._rank = ""

    # getter
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_sex(self):
        return self._sex

    def get_age(self):
        return self._age

    def get_sc_math(self):
        return self._sc_math

    def get_sc_physical(self):
        return self._sc_physical

    def get_sc_chemistry(self):
        return self._sc_chemistry

    def get_sc_average(self):
        return self._sc_average

    def get_rank(self):
        return self._rank

    # setter
    def set_id(self, my_id):
        self._id = my_id

    def set_name(self, name):
        self._name = name

    def set_sex(self, sex):
        self._sex = sex

    def set_age(self, age):
        self._age = age

    def set_sc_math(self, sc_math):
        self._sc_math = sc_math

    def set_sc_physical(self, sc_physical):
        self._sc_physical = sc_physical

    def set_sc_chemistry(self, sc_chemistry):
        self._sc_chemistry = sc_chemistry

    def set_sc_average(self, sc_average):
        self._sc_average = sc_average
