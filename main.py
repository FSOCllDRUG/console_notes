from notes_interaction import *
from menu import main_menu

Create()
with open('ascii-art.txt', 'r') as file:
    data = file.read()
print(data)
# table.field_names = lines[0]
main_menu()
# os.system('python menu.py')

exit()

