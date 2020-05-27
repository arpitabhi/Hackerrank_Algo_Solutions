#Author : Arpit Shukla
#Date : 28th May, 2020

#Hackerrank Matching Anything But a Newline Solution Python

regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())