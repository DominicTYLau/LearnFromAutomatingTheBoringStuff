# Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

import re

input = input("Enter a strong Password: ")

def isStrongPwd(pwd):
    if len(pwd) < 8:
        return False
    elif re.search('[a-z]', pwd) == None:
        return False
    elif re.search('[A-Z]', pwd) == None:
        return False
    elif re.search('\d', pwd) == None:
        return False
    return True

print(isStrongPwd(input))