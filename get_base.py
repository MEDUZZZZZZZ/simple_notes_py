import pathlib

csv_file_path = pathlib.Path('.', 'files', 'databse.csv')


def get_base():
    with open(csv_file_path, mode='r', encoding='utf-8') as db:
        data = db.readlines()  # notes_list = db.read().split('\n') альтераетив
        return data
