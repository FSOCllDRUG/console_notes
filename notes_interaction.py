import csv
from datetime import datetime
import os
import os.path

# import pandas as pd

# print("Date+Time =", current_date, "", current_time)
now = datetime.now()
current_date = now.strftime("%d:%m:%y")
current_time = now.strftime("%H:%M")
header = ['Id', 'Name', 'Date', 'Time', 'Note']
data = ['none', current_date, current_time, 'test']


# note_id = 0


# creating notes.csv if it doesn't exist
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
    print(len(lines))
    note_id = len(lines)
    # Create the dictionary (=row)
    row = {'Id': note_id, 'Name': note_name, 'Date': current_date, 'Time': current_time, 'Note': note_text}

    # Open the CSV file in "append" mode
    with open('notes.csv', 'a', newline='') as f:
        # Create a dictionary writer with the dict keys as column fieldnames
        writer = csv.DictWriter(f, fieldnames=row.keys())

        # Append single row to CSV
        writer.writerow(row)


def ViewNotes():
    with open('notes.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)



def EditNote():
    r = csv.reader(open('notes.csv'))
    lines = list(r)
    print(lines)
    e1 = int(input('Enter id: '))
    edited_note = str(input('Enter edited note: '))
    lines[e1][4] = edited_note
    writer = csv.writer(open('notes.csv', 'w', encoding='UTF8', newline=''))
    writer.writerows(lines)


def DeleteNote():
    r = csv.reader(open('notes.csv'))
    lines = list(r)
    print(lines)
    e1 = int(input('Enter id: '))
    lines.pop(e1)
    writer = csv.writer(open('notes.csv', 'w', encoding='UTF8', newline=''))
    writer.writerows(lines)

# AddNote()
