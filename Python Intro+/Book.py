from datetime import datetime, timedelta

l_genre = ['Action', 'Drama', "SCI-FI", "Biography", "Documentary", "Thriller"]

class Book(object):
    def __init__(self, name, author, date, genre):
        self.name = name
        self.author = author
        self.date = date
        self.genre = genre


    def set_genre(self, genre):
        if genre not in l_genre:
            return False, f"Invalid genre: {genre}.\nGenre should be on of the following:\nAction, Drama, SCI-FI, Biography, Documentary, Thriller"
        return True, ""

    def set_date(self, date_string):
        '''
        Date should be of format "%Y-%m-%d", example: 2023-08-07
        :param str_date: string representing date of format "%Y-%m-%d"
        :return: boolean, str
        '''
        date_format = "%Y-%m-%d"
        curr_date = datetime.now().date()
        try:
            date_object = (datetime.strptime(date_string, date_format)).date()
            if date_object > curr_date:
                return False, "Date should be earlier than today"
        except ValueError:
            return False, "Invalid Date format, date should be YYYY-MM-DD"

        return True, ""

