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

"""
Reviewer comments:
The previous reviewer mentioned this already, but using sets is extremely beneficial here. Not only because it can simplify your code because sets don't allow for duplicates, but also because it would be a more efficient approach.

Dictionaries and sets in python are implemented using hashmaps (underlying data structures, you might learn about them later in the ND). The worst-case scenario for item lookup or adding an item or removing one, is technically O(n).

However, that worst-case scenario rarely ever happens (if you want more details you can check this source - https://stackoverflow.com/questions/1963507/time-complexity-of-accessing-a-python-dict ). So for all purposes, it's more accurate to consider the average case scenario which is O(1).

And therefore you won't have a quadratic time complexity when using sets here.
"""
