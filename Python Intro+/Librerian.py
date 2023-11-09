from Human import Human


class Librarian(Human):
    def __init__(self, human, hourly_pay):
        self.name = human.get_name()
        self.surename = human.get_surename()
        self.id = human.get_id()
        self.age = human.get_age()
        self.hourly_pay = hourly_pay
        self.work_hours = 0


    def update_work_hours(self, number):
        try:
            hours = float(number)
            if hours < 0:
                return False, "Can't add negative value"
            else:
                if (self.work_hours + hours) > 186:
                    return False, "Can't work more than 186 hours"
                else:
                    self.work_hours += hours
                    return True, ""

        except ValueError:
            return False, "illegal value"

    def get_salary(self):
        return self.work_hours * self.hourly_pay


    def display_worker(self):
        return f"ID: {self.id}\nName: {self.name}\nSurename: {self.surename}\nAge: {self.age}\nHourly pay: {self.hourly_pay}\nWork hours: {self.work_hours}\nSalary: {self.get_salary()}"


def validate_librarian_age(age):
    try:
        age = float(age)
        if age > 17:
            return True, ""
        else:
            return False, "illegal age"
    except ValueError as e:
        return False, "Age must be numeric"



def validate_hourly_pay(hourly_pay):
    try:
        hourly_pay = float(hourly_pay)
        if hourly_pay > 20:  # Try to convert the string to a float
            return True, ""
        else:
            return False, "Hourly pay should be above 20 nis"
    except ValueError:
        return False, "Value is not a number"