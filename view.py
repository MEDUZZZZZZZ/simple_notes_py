import datetime
import note
from get_base import get_base


def ui_input(key: int):
    match key:
        case 1:
            message = "Введите запрос: "  # по этому запросу находим методом search(model) нужную нам заметку, показываем методом convert_to_output
        case 2:
            message = "Введите название заметки: "
        case 3:
            message = "Введите содержание заметки :"
        case 4:
            message = "Введите номер заметки: "
        case 5:
            message = "Выберите что изменить:\n\
            1 - изменить название\
            2 - изменить содержание\
            3 - изменить все\
            Введите: "
    return str(input(message))


def convert_to_output(sourse: str):
    tmp = sourse.split(";")
    res = f'Заметка id {tmp[0]} название: {tmp[1]} дата последнего изменения {tmp[3]}\n Содержание: \n{tmp[2]}\n '
    res += f"{'-'*20}\n"
    return res


def start_message():
    welcome = "Добро пожаловать в приложение заметки!\n\
Для работы вам могут пригодиться следющие команды:\
'show_al' - показать все заметки\
'search' - найти и показать заметку\
'add' - добавить заметку\
'edit' - изменить заметку\
'del' - удалить заметку\
'exit' - выйти из приложения\
\nВведите команду: "
    return str(input(welcome)).lower()

    
def show_all():
    res = ''
    notes_list = get_base()
    for c_note in notes_list:
        res += convert_to_output(c_note)
    return res


def user_add():
    header = ui_input(2)
    body = ui_input(3)
    tmp = [header, body]
    this_note = note.Note(tmp)
    return this_note

def ui_choose_note(sourse: list[str]):
    count = 0
    print(f'Нашлось {len(sourse)} заметок по вашему запросу\n')
    for c_note in sourse:
        count += 1
        print(f'{count}: {convert_to_output(c_note)}')
    choose = ui_input(4)
    if int(choose) <= len(sourse):
        return sourse[int(choose)]
    else:
        print("Вы ввели недопустимое: ")
        return ui_choose_note(sourse)


def ui_edit(mode: int, note_to_edit: str):
    new_note = note_to_edit.split(";")
    result = ''
    match mode:
        case "1":
            new_name = ui_input(2)
            new_note[1] = new_name

        case "2":
            new_body = ui_input(3)
            new_note[2] = new_body
        case "3":
            new_name = ui_input(2)
            new_body = ui_input(3)
            new_note[1] = new_name
            new_note[2] = new_body
    new_note[3] = datetime.datetime
    result = ";".join(new_note)
    print('Заметка успешно изменена')
    return result
    