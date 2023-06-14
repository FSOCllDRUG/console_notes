from notes_interaction import *

c1 = 'Create note'
c2 = 'Edit note'
c3 = 'Delete note'
c4 = 'Check notes'
c5 = 'Exit'

cv1 = 'Show all notes'
cv2 = 'Show notes for a specific date'
cv3 = 'Show one note'
cv4 = 'Back to main menu'

menu_options = {
    1: c1,
    2: c2,
    3: c3,
    4: c4,
    5: c5,
}
view_options = {
    1: cv1,
    2: cv2,
    3: cv3,
    4: cv4,
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def view_menu():
    for key in view_options.keys():
        print(key, '--', view_options[key])


def option1():
    print(c1, '\n')
    AddNote()
    main_menu()


def option2():
    print(c2, '\n')
    EditNote()
    main_menu()


def option3():
    print(c3, '\n')
    DeleteNote()
    main_menu()


def option4():
    print(c4, '\n')
    view_menu()
    choose_v_menu()


def option5():
    print(c5, '\n')


def v_option1():
    ViewNotes()
    main_menu()


def v_option2():
    InputDate()
    main_menu()


def v_option3():
    OneNote()
    main_menu()


def v_option4():
    main_menu()


def choose_v_menu():
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    # Check what choice was entered and act accordingly
    if option == 1:
        v_option1()
    elif option == 2:
        v_option2()
    elif option == 3:
        v_option3()
    elif option == 4:
        v_option4()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')


def main_menu():
    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    # Check what choice was entered and act accordingly
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        print('\nHave a good day!')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 5.')
