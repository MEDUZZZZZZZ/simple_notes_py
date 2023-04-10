import pathlib
import note
import re

csv_file_path = pathlib.Path('.', 'files', 'databse.csv')


def add_note(path: pathlib.WindowsPath, input: note.Note):
    with open(path, mode='ab', encoding='utf-8') as db:
        c_note = input.get_info()
        db.write(c_note)
        return 'New note successfully added'

        
def search_note(path: pathlib.WindowsPath, request: str):
    with open(path, mode='r', encoding='utf-8') as db:
# notes_list = db.read().split('\n') альтераетива
        notes_list = db.readlines()
        res = []
        flag = 0
        for c_note in notes_list:
            if request in c_note:
                res.append(c_note)
                flag = 1
        if flag != 1:
            res.append(f'Note by request: {request} not found') # Можетсделать возврат строки вместо добавления сообщения в список
        return res


def delete_note(path: pathlib.WindowsPath, request: str):
    to_delete = search_note(path, request)[0]
    # if 'not found' not in to_delete[0]: если вдруг решу все так реализовать это
    pattern = re.compile(re.escape(to_delete))
    with open(path, mode='r+', encoding='utf-8') as db:
        notes_list = db.readlines()
        db.seek(0)
        for c_note in notes_list:
            flag = pattern.search(c_note)
            if flag is None:
                db.write(c_note)
            db.truncate() 
    return "Selected note deleted"

def edit_note(path: pathlib.WindowsPath, request: str, edited: str):
    to_edit = search_note(path, request)[0]
    pattern = re.compile(re.escape(to_edit))
    with open(path, mode='r+', encoding='utf-8') as db: # вынести как отдельную функцию?
        notes_list = db.readlines()
        db.seek(0)
        for c_note in notes_list:
            flag = pattern.search(c_note)
            if flag is None:
                db.write(c_note)
            else:
                db.write(edited)
    return "Selected note edited"



def chose(option: list[str], pos: int):
    pass
