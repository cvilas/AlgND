"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import operator
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_spent = dict()
for record in calls:
    calling_number = record[0]
    receiving_number = record[1]
    duration = int(record[3])
    if calling_number in time_spent.keys():
        time_spent[calling_number] += duration
    else:
        time_spent[calling_number] = duration

    if receiving_number in time_spent.keys():
        time_spent[receiving_number] += duration
    else:
        time_spent[receiving_number] = duration

phone_number = max(time_spent, key=time_spent.get)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number, time_spent[phone_number]))