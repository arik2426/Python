from datetime import datetime, timedelta

from Human import Human
from Member import Member, Registration
from Book import Book
from Librerian import Librarian, validate_librarian_age, validate_hourly_pay
import re

class Library_class(object):
    def __init__(self):
        self.__members = []  # Members
        self.__books = {}  # {"book_name": numbers of book in library at the moment}
        self.__workers = []  # Librerians

    # def get_members(self):
    #     return self.__members

    def get_books(self):
        books = ""
        l_books = list(self.__books.keys())
        for book in l_books:
            books += f"{book}\n"
        return books

    def get_book(self,name):
        books = list(self.__books.keys())
        if name in books:
            book = self.__books[name][0]
            return book, f"Name: {book.name}\nAuthor: {book.author}\nDate: {book.date}\nGenre: {book.genre}\nAvailable: {self.__books[name][1]}"
        return None, f"{name} not found in library"

    def get_book_count(self,name):
        books = list(self.__books.keys())
        if name in books:
            return self.__books[name][1]
        return 0

    def borrow_book(self, name):
        self.__books[name][1] -= 1


    def display_members(self):
        members = ""
        for member in self.__members:
            members += f"{member.id} {member.name} {member.surename}\n"
        return members

    def search_member(self, id_):
        ret_member = None
        msg = ""
        for member in self.__members:
            if member.id == id_:
                # return member
                ret_member = member
                msg = ret_member.display_member()
                break
        if not ret_member:
            msg = f"Memeber with ID '{id_}' not found"

        return ret_member, msg

    def search_worker(self, id_):
        ret_worker = None
        msg = ""
        for worker in self.__workers:
            if worker.id == id_:
                ret_worker = worker
                msg = ret_worker.display_worker()
                break

        if not ret_worker:
            msg = f"Librarian wiht ID '{id_}' not found"
        return ret_worker, msg


    def display_workers(self):
        workers = ""
        for worker in self.__workers:
            workers += f"{worker.id} {worker.name} {worker.surename}\n"
        return workers

    def add_member(self, member):
        if isinstance(member, Member):
            self.__members.append(member)
            return True,""
        return False, "Not a member"

    def add_worker(self, worker):
        if isinstance(worker, Librarian):
            self.__workers.append(worker)
            return True, ""
        return False, "Not a Librarian"

    def add_book(self, book):
            books = list(self.__books.keys())
            if book.name not in books:
                self.__books[book.name] = [book, 1]
            else:
                self.__books[book.name][1] += 1


    def return_book(self, name):
        self.__books[name][1] += 1


    # def display_by_genre(self, genre):
    #     books = ""
    #     for book in self.__books:
    #         if book.get_genre() == genre:
    #             bookd += f"{book.get_name()}\n"
    #     return books

    def remove_member(self, id_):
        member, msg = self.search_member(id_)
        if member:
            full_name = f"{member.name} {member.surename}"
            self.__members.remove(member)
            return f"{full_name} removed successfully"
        else:
            return msg

    def remove_worker(self, id_):
        worker, msg = self.search_worker(id_)
        if worker:
            full_name = f"{worker.name} {worker.surename}"
            self.__workers.remove(worker)
            return f"{full_name} removed successfully"
        else:
            return msg

def create_human(name, surename, _id, age):
    err_msg = ""
    human_instance = Human(name, surename, _id, age)
    name_is_valid, err1 = human_instance.validate_name(name)
    if not name_is_valid:
        err_msg += err1
    surename_is_valid, err2 = human_instance.validate_surename(surename)
    if not surename_is_valid:
        err_msg += f"\n{err2}"
    id_is_valid, err3 = human_instance.validate_id(_id)
    if not id_is_valid:
        err_msg += f"\n{err3}"
    age_is_valid, err4 = human_instance.validate_age(age)
    if not age_is_valid:
        err_msg += f"\n{err4}"
    if name_is_valid and surename_is_valid and id_is_valid and age_is_valid:
        return human_instance, ""
    return None, err_msg


def create_member(inputs):

    human, err1 = create_human(inputs[1], inputs[2], inputs[0], inputs[3])
    if not human:
        return None, err1
    member = Member(human)

    return member, ""


def create_librerian(inputs):
    err_msg = ""
    human, err1 = create_human(inputs[1], inputs[2], inputs[0], inputs[3])

    if not human:
        return None, err1

    hourly_pay_is_valid, err2 = validate_hourly_pay(inputs[4])

    if not hourly_pay_is_valid:
        err_msg += f"\n{err2}"

    age_is_valid, err3 = validate_librarian_age(inputs[3])

    if not age_is_valid:
        err_msg += f"\n{err3}"

    if len(err_msg)==0:
        librerian = Librarian(human, float(inputs[4]))
        return librerian, ""

    return None, err_msg


def create_book(inputs):
    err_msg = ""
    book = Book(inputs[0], inputs[1], inputs[2], inputs[3])
    date_is_valid, date_err_msg = book.set_date(inputs[2])
    genre_is_valid, genre_err_msg = book.set_genre(inputs[3])

    if (not date_is_valid) or (not genre_is_valid):
        err_msg = f"{date_err_msg}\n{genre_err_msg}"
        return None, err_msg

    return book, ""

def get_borrow_date_and_return_date():
    current_date = datetime.now().date()
    return_date = current_date + timedelta(days=7)
    return current_date, return_date