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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print("First record of texts, {} texts {} at time {}".format(texts[0][0], texts[0][1], texts[0][2]))
last_call_index = len(calls)-1
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[last_call_index][0], calls[last_call_index][1], calls[last_call_index][2], calls[last_call_index][3]))

"""
Reviewer comments:

The previous reviewer already pointed out how you could simplify the above a bit.

Here is a good resource on a new feature called f-strings (https://cito.github.io/blog/f-strings/) for ptyhon 3.6 and higher and how they compare to something like the format function. There are certain advantages to them and can be useful to learn about.
"""
