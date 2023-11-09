import re

class Human(object):
    def __init__(self, name, surename, _id, age):
        self.__name = name
        self.__surename = surename
        self.__id = _id
        self.__age = age

    def validate_name(self, name):
        # Define the regular expression pattern
        pattern = r'^([A-Za-z])*$'

        # Use re.match to check if the name matches the pattern
        if re.match(pattern, name):
            return True, ""
        else:
            return False, "illegal name"


    def validate_surename(self, surename):
        # Define the regular expression pattern
        pattern = r"^[A-Za-z\-']*$"

        # Use re.match to check if the surname matches the pattern
        if re.match(pattern, surename):
            return True, ""
        else:
            return False, "illegal surname"

    def validate_age(self, age):
        try:
            age = float(age)
            if age > 9:
                return True, ""
            else:
                return False, "To Young, should be at least 10"
        except ValueError:
            return False, "illegal age"


    def validate_id(self, _id):
        pattern = r'[0-9]{9}'

        if re.match(pattern, _id):
            return True, ""
        else:
            return False, "illegal id"

    def get_name(self):
        return self.__name

    def get_surename(self):
        return self.__surename

    def get_age(self):
        return self.__age

    def get_id(self):
        return self.__id