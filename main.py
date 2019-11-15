#! /usr/bin/env python3

from mypackage.birthdays import return_birthday
import sys

if len(sys.argv) > 2:
    argument = str(sys.argv[1] + ' ' + sys.argv[2])
else:
    print("Please, enter a valid name (Name Surname)")
    exit()

return_birthday(argument)
