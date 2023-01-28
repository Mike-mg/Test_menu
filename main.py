import os


def main_menu():

    list_menu = ["Option 1", "Quit"]

    for item_id, item_menu in enumerate(list_menu):
        print(f"[ {item_id} ] {item_menu}")

    print()


def menu_2():

    list_menu = ["Option a", "Return Main Menu"]

    for item_id, item_menu in enumerate(list_menu):
        print(f"[ {item_id} ] {item_menu}")

    print()


def show_main_menu():

    os.system('clear')

    main_menu()

    while True:

        choice = int(input("> Choice option : "))

        if choice == 0:

            os.system('clear')

            menu_2()

            choice = int(input("> Choice option : "))

            if choice == 0:
                pass
            elif choice == 1:
                show_main_menu()

        else:
            return False


show_main_menu()
