import csv
from datetime import datetime
import os.path

# print("Date+Time =", current_date, "", current_time)
now = datetime.now()
current_date = now.strftime("%d:%m:%y")
current_time = now.strftime("%H:%M")
header = ['Name', 'Date', 'Time', 'Note']
data = ['none', current_date, current_time, 'test']


# creating notes.csv if it doesn't exist
def Create():
    if os.path.isfile('notes.csv') == False:
        with open('notes.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow([])


# Append notes.csv by adding new note(row)
def AddNote():
    notename = None
    # Create the dictionary (=row)
    row = {'name': notename, 'date': current_date, 'Time': current_time, }

    # Open the CSV file in "append" mode
    with open('notes.csv', 'a', newline='') as f:
        # Create a dictionary writer with the dict keys as column fieldnames
        writer = csv.DictWriter(f, fieldnames=row.keys())

        # Append single row to CSV
        writer.writerow(row)

# AddNote()
