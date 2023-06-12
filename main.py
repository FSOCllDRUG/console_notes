import csv
from datetime import datetime
# print("Date+Time =", current_date, "", current_time)
def NewNote():
    now = datetime.now()
    current_date = now.strftime("%d:%m:%y")
    current_time = now.strftime("%H:%M")
    header = ['name', 'date', 'time', 'note']
    data = ['none', current_date, current_time, 'test']

    with open('notes.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerow(data)

