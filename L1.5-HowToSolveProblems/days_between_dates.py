# Lesson 1.5 Days between dates
# Approach:
# - Conceptualise the solution using pseudo code, which would look something like this
# ```
# function daysBetweenDates(year1, month1, day1, year2, month2, day2):
#   while (year1, month1, day1) < (year2, month2, day2):
#       year1, month1, day1 = nextDay(year1, month1, day1)
#       days += 1
#   return days
# ```
# - Clarify assumptions: We use Gregorian calendar
# - Write helper function dateIsBefore()
# - Write a stub function daysInMonth(year, month) that always returns 30
# - Write nextDay(y, m, d) that uses daysInMonth() to return the next date
# - Write test harness for nextDay(). Test it.
# - Modify daysInMonth() to be correct, except for leap years
# - Test nextDay() again
# - Write IsLeapYear()
# - Write test harness for IsLeapYear()
# - Modify daysInMonth() to handle leap year

def isLeapYear(year):
    if ((year % 4 is 0) and (year % 100 is not 0)) \
    or (year % 400 is 0):
        return True
    
    return False


def daysInMonth(year, month):
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    
    if month in {1,3,5,7,8,10,12}:
        return 31

    return 30

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()
