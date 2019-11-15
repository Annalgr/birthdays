#! /usr/bin/env python3

from mypackage.birthdays import return_birthday
import sys

if len(sys.argv) > 1:
    argument = sys.argv[1]
else:
    print("Give me an argument to print")
    exit()

return_birthday(argument)
