import view
import model


def run_app():
    while True:
        mode = view.start_message()
        match mode:
            case "show_all":
                print(view.show_all)
            case "search":
                tmp = model.search_note(view.ui_input(1))
                if len(tmp) > 1:
                    res = view.ui_choose_note(tmp)
                    print(view.convert_to_output(res))
                elif 'not found' in tmp[0]:
                    res = tmp[0]
                    print(res)
                    continue
                else:
                    res = view.convert_to_output(tmp[0])
                    print(res)
            case "add":
                new_note = view.user_add()
                print(model.add_note(new_note))
            case "edit":
                tmp = model.search_note(view.ui_input(1))
                if len(tmp) > 1:
                    res = view.ui_choose_note(tmp)
                elif 'not found' in tmp[0]:
                    res = tmp[0]
                    print(res)
                    continue
                else:
                    res = tmp[0]
                new_note = view.ui_edit(res)
                print(model.edit_note(res, new_note))
            case "del":
                tmp = model.search_note(view.ui_input(1))
                if len(tmp) > 1:
                    res = view.ui_choose_note(tmp)
                elif 'not found' in tmp[0]:
                    res = tmp[0]
                    print(res)
                    continue  # Поменять
                else:
                    res = tmp[0]
                print(model.delete_note(res))
            case "exit":
                break
            case _:
                print('Не верная команда')
