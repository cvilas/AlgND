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

"""
Reviewer comments:

Instead of the current approach you can use python's built-ins/standard libraries to simplify things for you. The defaultdict from the collections library can be used for building a dictionary where if a key already exists the value is modified in some way, but if the key doesn’t exist some type of default value is entered

from collections import defaultdict

call_dict = defaultdict(int)
for call in calls:
    call_dict[call[0]] += int(call[3])
    call_dict[call[1]] += int(call[3])

Defaultdict will automatically fill in missing keys with when required.
"""
