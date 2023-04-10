class Note:
    i = 0

    def __init__(self, data_list):
        self.__class__.i += 1
        self.i = self.__class__.i
        self.head = data_list[0]
        self.body = data_list[1]

    @classmethod
    def cur_id_getter(cls):
        return cls.i
