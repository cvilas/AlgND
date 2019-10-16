"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_numbers = []
for record in texts:
    calling_number = record[0]
    receiving_number = record[1]
    if calling_number not in unique_numbers:
        unique_numbers.append(calling_number)
    if receiving_number not in unique_numbers:
        unique_numbers.append(receiving_number)

for record in calls:
    calling_number = record[0]
    receiving_number = record[1]
    if calling_number not in unique_numbers:
        unique_numbers.append(calling_number)
    if receiving_number not in unique_numbers:
        unique_numbers.append(receiving_number)

print("There are {} different telephone numbers in the records.".format(len(unique_numbers)))