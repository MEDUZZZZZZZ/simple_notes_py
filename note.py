import datetime


class Note:
    i = 0

    def __init__(self, data_list):
        self.__class__.i += 1
        self.i = self.__class__.i
        self.head = data_list[0]
        self.body = data_list[1]
        self.date = datetime.datetime

    def get_h(self):
        return self.head

    def get_b(self):
        return self.body

    def get_d(self):
        return self.date

    @classmethod
    def get_id(cls):
        return cls.i
