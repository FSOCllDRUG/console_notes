import csv
import os
import os.path
# import platform
import re
from prettytable import PrettyTable
from datetime import datetime

now = datetime.now()
current_date = now.strftime("%d.%m.%y")
current_time = now.strftime("%H:%M")
header = ['Id', 'Name', 'Date', 'Time', 'Note']
data = ['none', current_date, current_time, 'test']

# r = csv.reader(open('notes.csv'))
# lines = list(r)

table = PrettyTable()

#  InputDate()
pattern = r'\d{1,2}\.\d{2}\.\d{2}'  # Setting a pattern for input
regex = re.compile(pattern)
#

# SearchV()
selected_date = []  # Creating a list for confirmed notes(rows)
empty = 'No notes were created on this date.'  # Error messages if no notes(rows) for entered date


# date = None #Creating empty date


#

# Creating notes.csv if it doesn't exist
def Create():
    if os.path.isfile('notes.csv') == False:
        with open('notes.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            # writer.writerow([])


# Append notes.csv by adding new note(row)
def AddNote():
    r = csv.reader(open('notes.csv'))
    note_name = input('Note name:  ')
    note_text = input('Note text:  ')
    lines = list(r)
    note_id = len(lines)
    # Create the dictionary (=row)
    row = {'Id': note_id, 'Name': note_name, 'Date': current_date, 'Time': current_time, 'Note': note_text}

    # Open the CSV file in "append" mode
    with open('notes.csv', 'a', newline='') as f:
        # Create a dictionary writer with the dict keys as column fieldnames
        writer = csv.DictWriter(f, fieldnames=row.keys())

        # Append single row to CSV
        writer.writerow(row)


# Function for printing out existing notes
def ViewNotes():
    r = csv.reader(open('notes.csv'))
    lines = list(r)
    table = PrettyTable()
    table.field_names = lines[0]
    table.add_rows(lines[1:])
    print(table)


# Function for editing selected note by id
def EditNote():
    r = csv.reader(open('notes.csv'))
    lines = list(r)
    print(lines)
    e1 = int(input('Enter id: '))
    edited_note = str(input('Enter edited note: '))
    lines[e1][4] = edited_note
    lines[e1][2] = current_date
    lines[e1][3] = current_time
    writer = csv.writer(open('notes.csv', 'w', encoding='UTF8', newline=''))
    writer.writerows(lines)


# Function for deleting selected by id note
def DeleteNote():
    r = csv.reader(open('notes.csv'))
    lines = list(r)
    print(lines)
    e1 = int(input('Enter id: '))
    lines.pop(e1)
    writer = csv.writer(open('notes.csv', 'w', encoding='UTF8', newline=''))
    writer.writerows(lines)


# Clear terminal screen function for unix and windows oses
# def ClearScreen():
#     if os.name == 'nt':
#         os.system('cls')
#     elif os.name == 'posix':
#         os.system('clear')
#     elif os.name == 'java':
#         os.system('cls')
#     else:
#         print("\n")

# if platform == 'Windows':
#     input('Press <Enter> to return in menu...')
#     os.system('CLS')
# else:
#     input('Press <Enter> to return in menu...')
#     os.system('clear')


def InputDate():
    date = input('Enter the date: ')
    match = regex.search(date)
    if match:
        SearchV(date)
    else:
        print("Wrong format! Enter text in the format xx.xx.xx or x.xx.xx")


def SearchV(date):
    r = csv.reader(open('notes.csv'))
    lines = list(r)
    table = PrettyTable()
    ec = 0
    for item in list(lines):
        # print(item)
        if date in item:
            # print(item)
            selected_date.append(item)
            ec += 1
    if ec != 0:
        # for item in list(selected_date):
        #     print(item)
        # for sublist in selected_date:
        # print(' '.join(sublist))
        # table.field_names = lines[0]
        table.add_rows(selected_date)
        print(table)

    else:
        print(empty)


def OneNote():
    r = csv.reader(open('notes.csv'))
    lines = list(r)
    table = PrettyTable()
    on = int(input('Enter note ID to view it: '))
    print(lines)
    table.field_names = lines[0]
    table.add_row(lines[on])
    print(table)

# table = PrettyTable()
# InputDate()
