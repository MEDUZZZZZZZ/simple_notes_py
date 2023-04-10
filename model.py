import pathlib
import datetime
import note
csv_file_path = pathlib.Path('.', 'files', 'databse.csv')


def add_note(path: pathlib.WindowsPath, input: note.Note):
    with open(path, mode='ab', encoding='utf-8') as db:
        c_note = f'{input.get_id()};{input.get_h()};{input.get_b()};{input.get_d()}'
        db.write(c_note)

        
def search_note():
    pass

def delete_note():
    pass

def edit_note():
    pass

def convert():
    pass


