import note
from get_base import get_base, get_base_last_id
from datetime import datetime
from os import system


def welcome():
    system("cls")
    print("Добро пожаловать в приложение заметки!\n")


def start_message():
    return ui_input(0)


def ui_input(key: int):
    match key:
        case 0:
            message = "Для работы вам могут пригодиться следющие команды:\n\
'show_all' - показать все заметки \
'search' - найти и показать заметку \
'add' - добавить заметку\n\
'edit' - изменить заметку \
'del' - удалить заметку \
'exit' - выйти из приложения \
\nВведите команду: "
        case 1:
            message = "Введите запрос для поиска: "
        case 2:
            message = "Введите название заметки: "
        case 3:
            message = "Введите содержание заметки :"
        case 4:
            message = "Введите номер заметки: "
        case 5:
            message = "Выберите что изменить:\n\
            1 - изменить название 2 - изменить содержание 3 - изменить все\n\
            Введите: "
        case 6:
            message = "Введите:\n1 - 'да'\n2 - 'нет'\n:"
        case 7:
            message = "\nВведите год дату в формате ггггммдд: "
        case 8:
            message = "\nПровести поиск с фильтрацией по дате?\n1 - 'да'\n2 - 'нет'\n:"
    return str(input(message)).strip()


def convert_to_output(sourse: str):
    tmp = sourse.split(";")
    res = f"id {tmp[0]} Название: {tmp[1]} дата последнего изменения {tmp[3]}\nСодержание:\n{tmp[2]}\n"
    res += f"{'-'*len(res)}\n"
    return res


def show_one(sourse: str):
    print(f"\n Нашел:\n{convert_to_output(sourse)}\n")


def show_all(flag: str):
    try:
        res = ""
        notes_list = get_base()
        match flag:
            case "1":
                filter = convert_date()
                for c_note in notes_list:
                    if filter in c_note:
                        res += convert_to_output(c_note)
            case "2":
                for c_note in notes_list:
                    res += convert_to_output(c_note)
            case _:
                res = "\nВвидимо вы ввели, что-то не так\n"
        if res != "":
            print(res)
        else:
            print("\n Заметок для данной даты не найдено\n")
    except FileNotFoundError:
        print("\nНа данный момент нет ни одной заметки, попробуй создать с помощью 'add'\n")


def user_add():
    last_id = get_base_last_id()
    header = ui_input(2)
    body = ui_input(3)
    if (header.find(';') or body.find(';')) != -1:
        print("\nПрошу вас не использовать символ ';', это мешает моей работе\n")
        return user_add()
    else:
        tmp = [header, body]
        return note.Note(tmp, last_id)


def ui_edit(note_to_edit: str):
    new_note = note_to_edit.split(";")
    result = ''
    mode = ui_input(5)
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
        case _:
            print("\nВы ввели не верную команду\n")
    new_note[3] = str(datetime.date(datetime.today()))
    result = ";".join(new_note)
    return result


def ui_show_some(sourse: list[str]):
    count = 0
    res = f"\nНашлось {len(sourse)} заметок по вашему запросу\n"
    for c_note in sourse:
        count += 1
        res += f'{count}: {convert_to_output(c_note)}'
    print(res)


def ui_choose_note(sourse: list[str]):
    choose = int(ui_input(4))
    if 1 <= choose <= len(sourse):
        return sourse[choose-1]
    else:
        print("\nВы ввели не допустимое значение\n")
        return ui_choose_note(sourse)


def ui_aprove():
    print("Подтверждаете действие?")
    btn = ui_input(6)
    match btn:
        case "1":
            print("\nДействие подтверждено\n")
            return True
        case "2":
            print("\nДействие отменено\n")
            return False
        case _:
            print("Несанкционированный ввод")
            return ui_aprove()


def convert_date():
    date = ui_input(7)
    if date.isdigit() and len(date) == 8:
        date = f'{date[:4]}-{date[4:6]}-{date[6:]}'
        return date
    else:
        print("\nПрошу писать дату только цифрами в указанном формате\n")
        return convert_date()
