import tkinter as tk
from tkinter import messagebox

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library App")

        self.root.geometry("300x200")

        self.students = []
        self.authors = []

        # Create GUI elements
        self.label = tk.Label(root, text="Library App", font=("Arial", 16))
        self.label.pack()

        self.add_student_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_student_button.pack()

        self.add_author_button = tk.Button(root, text="Add Author", command=self.add_author)
        self.add_author_button.pack()

        self.display_students_button = tk.Button(root, text="Display Students", command=self.display_students)
        self.display_students_button.pack()

        self.display_authors_button = tk.Button(root, text="Display Authors", command=self.display_authors)
        self.display_authors_button.pack()

    def add_student(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        gender = input("Enter student gender: ")
        student_id = input("Enter student ID: ")

        student = Student(name, age, gender, student_id)
        self.students.append(student)

        messagebox.showinfo("Success", "Student added successfully!")

    def add_author(self):
        name = input("Enter author name: ")
        age = int(input("Enter author age: "))
        gender = input("Enter author gender: ")

        author = Author(name, age, gender)
        self.authors.append(author)

        messagebox.showinfo("Success", "Author added successfully!")

    def display_students(self):
        if not self.students:
            messagebox.showinfo("Empty", "No students found.")
            return

        students_info = "Students:\n"
        for student in self.students:
            students_info += f"Name: {student.name}, Age: {student.age}, Gender: {student.gender}, Student ID: {student.student_id}\n"

        messagebox.showinfo("Students", students_info)

    def display_authors(self):
        if not self.authors:
            messagebox.showinfo("Empty", "No authors found.")
            return

        authors_info = "Authors:\n"
        for author in self.authors:
            authors_info += f"Name: {author.name}, Age: {author.age}, Gender: {author.gender}\n"
            if author.books:
                authors_info += "Books:\n"
                for book in author.books:
                    authors_info += f" - {book}\n"

        messagebox.showinfo("Authors", authors_info)


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Student(Human):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


class Author(Human):
    def __init__(self, name, age, gender, books=[]):
        super().__init__(name, age, gender)
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def display_info(self):
        super().display_info()
        if self.books:
            print("Books:")
            for book in self.books:
                print(f" - {book}")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
