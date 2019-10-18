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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
unique_callers = []
unique_texters = []
unique_text_receivers = []
unique_call_receivers = []

for record in calls:
    if record[0] not in unique_callers:
        unique_callers.append(record[0])
    if record[1] not in unique_call_receivers:
        unique_call_receivers.append(record[1])

for record in texts:
    if record[0] not in unique_texters:
        unique_texters.append(record[0])
    if record[1] not in unique_call_receivers:
        unique_text_receivers.append(record[1])

potential_telemarketers = []
for phone_number in unique_callers:
    if phone_number in unique_texters:
        continue
    if phone_number in unique_call_receivers:
        continue
    if phone_number in unique_text_receivers:
        continue
    potential_telemarketers.append(phone_number)

potential_telemarketers.sort()
print("These numbers could be telemarketers: ")
print(*potential_telemarketers, sep="\n")

