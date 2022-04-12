""" Sample Input
chris alan
Sample Output
Chris Alan
"""

"start"
#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    s = s.title()
    return s

OR


def solve(s):
    s =' '.join(w.capitalize() for w in s.split(' '))
    return s
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
"end"
