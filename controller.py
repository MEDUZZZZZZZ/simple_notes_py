import view
import model


def run_app():
    view.welcome()
    while True:
        buttn = view.start_message()
        match buttn.lower():
            case "show_all":
                view.show_all(view.ui_input(8))
            case "search":
                tmp = model.search_note(view.ui_input(1))
                if len(tmp) > 1:
                    view.ui_show_some(tmp)
                    target = view.ui_choose_note(tmp)
                    view.show_one(target)
                elif "не найдена" in tmp[0]:
                    print(tmp[0])
                else:
                    view.show_one(tmp[0])
            case "add":
                new_note = view.user_add()
                access = view.ui_aprove()
                match access:
                    case True:
                        res_note = model.add_note(new_note)
                        print(res_note)
                    case _:
                        continue
            case "edit":
                tmp = model.search_note(view.ui_input(1))
                if len(tmp) > 1:
                    view.ui_show_some(tmp)
                    target = view.ui_choose_note(tmp)
                elif "не найдена" in tmp[0]:
                    print(tmp[0])
                    continue
                else:
                    target = tmp[0]
                view.show_one(target)
                edited_note = view.ui_edit(target)
                access = view.ui_aprove()
                match access:
                    case True:
                        res_note = model.edit_note(target, edited_note)
                        print(res_note)
                    case _:
                        continue
            case "del":
                tmp = model.search_note(view.ui_input(1))
                if len(tmp) > 1:
                    view.ui_show_some(tmp)
                    target = view.ui_choose_note(tmp)
                elif "не найдена" in tmp[0]:
                    print(tmp[0])
                    continue
                else:
                    target = tmp[0]
                view.show_one(target)
                access = view.ui_aprove()
                match access:
                    case True:
                        deleted_note = model.delete_note(target)
                        print(deleted_note)
                    case _:
                        continue
            case "exit":
                break
            case _:
                print("\nНе верная команда\n")
