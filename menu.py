from notes_interaction import *

c1 = 'Create note'
c2 = 'Edit note'
c3 = 'Delete note'
c4 = 'All notes'
c5 = 'Exit'
menu_options = {
    1: c1,
    2: c2,
    3: c3,
    4: c4,
    5: c5,
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    print(c1,'\n')
    AddNote()

def option2():
    print('Handle option \'Option 2\'')


def option3():
    print('Handle option \'Option 3\'')


if __name__ == '__main__':
    while (True):
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
            option()
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
