import pathlib
# import os.path
import note
import re
from get_base import get_base

csv_file_path = pathlib.Path(pathlib.Path.cwd(), 'db', 'database.csv')
# csv_file_path = os.path.abspath('db\database.csv')


def add_note(input: note.Note, path=csv_file_path):
    with open(path, mode='a', encoding='utf-8') as db:
        c_note = input.get_info()
        db.write(f'{c_note}\n')
        return 'Новая заметка добавлена\n'


def search_note(request: str):
    notes_list = get_base()
    res = []
    flag = 0
    for c_note in notes_list:
        if request in c_note:
            res.append(c_note)
            flag = 1
    if flag != 1:
        res.append(f"Заметка по запросу: {request} не найдена")
    return res


def delete_note(request: str, path=csv_file_path):
    to_delete = search_note(request)[0]
    pattern = re.compile(re.escape(to_delete))
    notes_list = get_base()
    with open(path, mode='w', encoding='utf-8') as db:
        for c_note in notes_list:
            flag = pattern.search(c_note)
            if flag is None:
                db.write(c_note)
            db.truncate()
    return "Выбранная заметка удалена\n"


def edit_note(request: str, edited: str, path=csv_file_path):
    to_edit = search_note(request)[0]
    pattern = re.compile(re.escape(to_edit))
    notes_list = get_base()
    with open(path, mode='w', encoding='utf-8') as db:
        for c_note in notes_list:
            flag = pattern.search(c_note)
            if flag is None:
                db.write(c_note)
            else:
                db.write(edited)
                db.write('\n')
    return "Выбранная заметка удалена\n"
