# Enter your code here. Read input from STDIN. Print output to STDOUT

# Author : Arpit Shukla
# 24th May, 2020

import re

char=input()

# Solution 1 
m=re.search('(([a-zA-Z0-9]))\\1+',char)

# Solution 2 
m=re.search('(\w(?!_))\\1+',char)

print(m.group(1) if m else "-1")