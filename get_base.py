import pathlib

csv_file_path = pathlib.Path('.', 'simple_notes_py', 'files', 'database.csv')


def get_base():
    with open(csv_file_path, mode='r', encoding='utf-8') as db:
        data = db.readlines()  # notes_list = db.read().split('\n') альтераетив
        return data


def get_base_last_id():
    with open(csv_file_path, mode='a+', encoding='utf-8') as db:
        db.seek(0)
        data = db.readlines()
        if len(data) >= 1:
            last_note = data[len(data)-1]
            last_id = last_note.split(';')[0]
            return int(last_id)
        else:
            return 0
