import pathlib
import note
import re
from get_base import get_base

csv_file_path = pathlib.Path('.', 'files', 'databse.csv')


def add_note(input: note.Note, path=csv_file_path):
    with open(path, mode='ab', encoding='utf-8') as db:
        c_note = input.get_info()
        db.write(c_note)
        return 'New note successfully added'


def search_note(request: str):
    notes_list = get_base()
    res = []
    flag = 0
    for c_note in notes_list:
        if request in c_note:
            res.append(c_note)
            flag = 1
    if flag != 1:
        res.append(f'Note by request: {request} not found')
    return res


def delete_note(request: str, path=csv_file_path):
    to_delete = search_note(request)[0]
    pattern = re.compile(re.escape(to_delete))
    notes_list = get_base(path)
    with open(path, mode='w', encoding='utf-8') as db:
        for c_note in notes_list:
            flag = pattern.search(c_note)
            if flag is None:
                db.write(c_note)
            db.truncate()
    return "Selected note deleted"


def edit_note(request: str, edited: str, path=csv_file_path):
    to_edit = search_note(request)[0]
    pattern = re.compile(re.escape(to_edit))
    notes_list = get_base(path)
    with open(path, mode='w', encoding='utf-8') as db:
        for c_note in notes_list:
            flag = pattern.search(c_note)
            if flag is None:
                db.write(c_note)
            else:
                db.write(edited)
    return "Selected note edited"
