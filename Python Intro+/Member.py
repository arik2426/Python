from Human import Human

class Registration(object):
    def __init__(self, book_name, take_date, return_date):
        self.book_name = book_name
        self.take_date = take_date
        self.return_date = return_date

class Member(Human):
    def __init__(self, human):
        self.id = human.get_id()
        self.name = human.get_name()
        self.surename = human.get_surename()
        self.age = human.get_age()
        self.__registrations = []

    def borrow_book(self, book_name, take_date, return_date):
        self.__registrations.append(Registration(book_name, take_date, return_date))

    def return_book(self, book_name):
        book_found = False
        for reg in self.__registrations:
            if reg.book_name == book_name:
                self.__registrations.remove(reg)
                book_found = True
                break
        if not book_found:
            return f"i don't have this {book_name}"
        else:
            return ""

    def display_registrations(self):
        regs = ""
        for reg in self.__registrations:
            regs += f"\nBook: {reg.book_name}, Borrowed at: {reg.take_date}, Return date: {reg.return_date}"

        return regs

    def display_member(self):
        return f"ID: {self.id}\nName: {self.name}\nSurename: {self.surename}\nAge: {self.age}\nRegistrations: {self.display_registrations()}"
