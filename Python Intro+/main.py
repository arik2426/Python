
import tkinter as tk
from tkinter import simpledialog, messagebox
import Librery
from Librery import Library_class
from Human import Human
from Member import Member
from Book import Book
from Librerian import Librarian

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title, options):
        super().__init__(parent)
        self.title(title)
        self.result = None

        for option in options:
            button = tk.Button(self, text=option, command=lambda o=option: self.on_button_click(o))
            button.pack()

    def on_button_click(self, option):
        self.result = option
        self.destroy()


class CustomInputDialog(tk.Toplevel):
    def __init__(self, parent, title, options):
        super().__init__(parent)
        self.title(title)
        self.input_field_list = []
        self.values_list = []

        for option in options:
            instruction_label = tk.Label(self, text=f"{option}:")
            instruction_label.pack(pady=10)

            input_field = tk.Entry(self)
            input_field.pack(pady=5)
            self.input_field_list.append(input_field)

        submit_button = tk.Button(self, text="Submit", command=self.on_button_click)
        submit_button.pack(pady=10)

    def on_button_click(self):
        for field in self.input_field_list:
            self.values_list.append(field.get())
        self.destroy()

class LibraryUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library System")

        # Create and place the "Library" label at the top
        self.library_label = tk.Label(root, text="Library", font=("Helvetica", 20))
        self.library_label.pack(pady=20)

        # Create and place the buttons for "Book", "Member", and "Librarian"
        self.create_button("Book", ["Add", "Borrow", "Return", "Search", "Display"])
        self.create_button("Member", ["Add", "Remove", "Search", "Display"])
        self.create_button("Librarian", ["Add", "Remove", "Search", "Display", "Add work hours"])

    def create_button(self, text, options):
        button = tk.Button(self.root, text=text, width=15, height=3, command=lambda: self.show_actions(text, options))
        button.pack(pady=10)


    def handle_custom_input_dialog(self, selected_option, category, label):
        title = f"{selected_option} {category}"
        input_dialog = CustomInputDialog(self.root, title, label)
        self.root.wait_window(input_dialog)
        return input_dialog


    def handle_search(self, selected_option, category, label, func):
        input_dialog = self.handle_custom_input_dialog(selected_option, category, label)
        if len(input_dialog.values_list):
            obj, msg = func(input_dialog.values_list[0])
            messagebox.showinfo(f"{selected_option} {category}", msg)

    def handle_display(self, category, func):
        msg = func()
        title = f"Display {category}"
        if msg:
            messagebox.showinfo(title, msg)
        else:
            messagebox.showinfo(title, f"No {category}")

    def handle_remove(self, selected_option, category, func):
        input_dialog = self.handle_custom_input_dialog(selected_option, category, ["ID"])
        if len(input_dialog.values_list):
            msg = func(input_dialog.values_list[0])
            messagebox.showinfo(f"{selected_option} {category}", msg)

    def handle_add(self, selected_option, category, add_options, func_create, func_add):
        title = f"{selected_option} {category}"
        input_dialog = self.handle_custom_input_dialog(selected_option, category, add_options)
        if len(input_dialog.values_list):
            obj, msg = func_create(input_dialog.values_list)

            if obj:
                func_add(obj)
                if isinstance(obj, Book):
                    messagebox.showinfo(title, f"{obj.name} added successfully")
                else:
                    messagebox.showinfo(title, f"{obj.name} {obj.surename} added successfully")
            else:
                messagebox.showinfo(title, msg)

    def show_actions(self, category, options):
        dialog = CustomDialog(self.root, f"{category} Actions", options)
        self.root.wait_window(dialog)

        selected_option = dialog.result

        if category == "Member":
            if selected_option == "Add":
                self.handle_add(selected_option, category, ["ID", "Name", "Surname", "Age"], Librery.create_member, lib.add_member)

            if selected_option == "Display":
                self.handle_display(category, lib.display_members)

            if selected_option == "Search":
                self.handle_search(selected_option, category, ["ID"], lib.search_member)

            if selected_option == "Remove":
                self.handle_remove(selected_option, category, lib.remove_member)

        if category == "Librarian":
            if selected_option == "Add":
                self.handle_add(selected_option, category, ["ID", "Name", "Surname", "Age", "Hourly pay"], Librery.create_librerian,
                                lib.add_worker)

            if selected_option == "Search":
                self.handle_search(selected_option, category, ["ID"], lib.search_worker)


            if selected_option == "Display":
                self.handle_display(category, lib.display_workers)

            if selected_option == "Remove":
                self.handle_remove(selected_option, category, lib.remove_worker)


            if selected_option == "Add work hours":
                input_dialog = self.handle_custom_input_dialog(selected_option, category, ["ID", "Hours"])

                if len(input_dialog.values_list):
                    found_worker, msg = lib.search_worker(input_dialog.values_list[0])
                    if found_worker:
                        success, err_msg = found_worker.update_work_hours(input_dialog.values_list[1])
                        if not success:
                            messagebox.showinfo("Message Dialog", err_msg)
                        else:
                            messagebox.showinfo("Message Dialog", "Hours added successfully")
                    else:
                        messagebox.showinfo("Message Dialog", f"Librarian with ID: {input_dialog.values_list[0]} not found")

        if category == "Book":
            if selected_option == "Add":
                self.handle_add(selected_option, category, ["Name", "Author", "Date", "Genre"], Librery.create_book, lib.add_book)

            if selected_option == "Display":
                self.handle_display(category, lib.get_books)

            if selected_option == "Search":
                self.handle_search(selected_option, category, ["Book Name"], lib.get_book)

            if selected_option == "Borrow":
                # input_dialog = CustomInputDialog(self.root, f"{selected_option} {category}", ["Book Name", "Member ID"])
                # self.root.wait_window(input_dialog)
                input_dialog = self.handle_custom_input_dialog(selected_option, category, ["ID", "Hours"])

                if len(input_dialog.values_list):
                    book, msg = lib.get_book(input_dialog.values_list[0])
                    found_member, msg = lib.search_member(input_dialog.values_list[1])

                    if not book:
                        messagebox.showinfo("Book search result", msg)
                        return
                    if lib.get_book_count(input_dialog.values_list[0]) < 1:
                        messagebox.showinfo("Book availability", f"{input_dialog.values_list[0]} is not available at the moment")
                        return
                    if not found_member:
                        messagebox.showinfo("Message Dialog", f"Memeber with ID: {input_dialog.values_list[1]} not found")
                        return

                        lib.borrow_book(input_dialog.values_list[0])
                        borrow_date, return_date = Librery.get_borrow_date_and_return_date()
                        found_member.borrow_book(input_dialog.values_list[0], borrow_date, return_date)
                        messagebox.showinfo("Message Dialog", f"{input_dialog.values_list[0]} borrowed by {found_member.name} {found_member.surename} successfully")

            if selected_option == "Return":
                # input_dialog = CustomInputDialog(self.root, f"{selected_option} {category}", ["Book Name", "Member ID"])
                # self.root.wait_window(input_dialog)
                input_dialog = self.handle_custom_input_dialog(selected_option, category, ["ID", "Hours"])

                if len(input_dialog.values_list):
                    book, msg = lib.get_book(input_dialog.values_list[0])
                    found_member, msg = lib.search_member(input_dialog.values_list[1])

                    if not book:
                        messagebox.showinfo("Book search result", msg)
                        return

                    if not found_member:
                        messagebox.showinfo("Message Dialog", f"Memeber with ID: {input_dialog.values_list[1]} not found")
                        return

                    ret_msg = found_member.return_book(input_dialog.values_list[0])
                    if ret_msg:
                        messagebox.showinfo("Book return", ret_msg)
                        return

                    lib.return_book(input_dialog.values_list[0])

if __name__ == "__main__":
    human1 = Human("Avi", "Neelavi", "123456789", "29")
    human2 = Human("Sheli", "Kasheli", "987654321", "29")
    member = Member(human1)
    worker = Librarian(human2,hourly_pay=30)
    book = Book("Bible", "Moses", "1900-01-01", "Documentary")
    lib = Library_class()
    lib.add_book(book)
    lib.add_member(member)
    lib.add_worker(worker)

    root = tk.Tk()
    app = LibraryUI(root)
    root.mainloop()
