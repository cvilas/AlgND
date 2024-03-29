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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
unique_calls_to = []
num_calls_from_080 = 0
num_calls_from_080_to_080 = 0
for record in calls:
    if "(080)" in record[0]: # calling number is from Bangalore
        num_calls_from_080 += 1

        # if fixed line, extract area code which is in brackets
        # if mobile number extract area code which is first four digits if starting with [7,8,9]
        # # We can ignore telemarketers (area code 140) because they never receive calls

        # this will either extract digits in parenthesis or the entire number (10 digits)
        area_code = record[1][record[1].find("(")+1:record[1].find(")")]
        if len(area_code) is 10:
            area_code = area_code[0:4]
        if area_code not in unique_calls_to:
            unique_calls_to.append(area_code)
        if "080" == area_code:  # called number is also Bangalore based
            num_calls_from_080_to_080 += 1

unique_calls_to.sort()
print("The numbers called by people in Bangalore have codes:")
print(*unique_calls_to, sep="\n")

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

percent = 100. * num_calls_from_080_to_080/float(num_calls_from_080)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percent,2)))

"""
Reviewer comments:

You can convert a list into a set simply by doing set(list_name) later. So if you convert your unique_calls_to list to a set, all the duplicate values will get removed. And you can do this outside of the loop, right at the end, which separates out the need for this check and thereby saves on efficiency since converting a list to a set is not that computationally expensive either compared to the somewhat quadratic complexity you get now (more on this in the analysis file review)

"""
