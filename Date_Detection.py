
# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.
# The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

import re

input = input("Enter a Date in the format dd/mm/yyyy: ")

dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
mo = dateRegex.search(input)

day, month, year = mo.groups()


day = int(day)
month = int(month)
year = int(year)



def isValidDate(day, month, year):
    if day > 31:
        return False
    elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        return False
    elif month == 2:
        if year % 400 == 0 and day > 29:
            return False
        elif year % 100 == 0 and day > 28:
            return False
        elif year % 4 == 0 and day > 29:
            return False
    return True
    
print(isValidDate(day, month, year))


