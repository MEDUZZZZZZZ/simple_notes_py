from datetime import datetime


class Note:
    i = 0

    def __init__(self, data_list, cur_id=0):
        self.__class__.i = cur_id + 1
        self.i = self.__class__.i
        self.head = data_list[0]
        self.body = data_list[1]
        self.date = str(datetime.date(datetime.today()))

    def get_h(self):
        return self.head

    def get_b(self):
        return self.body

    def get_d(self):
        return self.date

    def get_info(self, cur_id=0):
        return f'{self.i};{self.head};{self.body};{self.date}'

    @classmethod
    def get_id(cls):
        return cls.i
