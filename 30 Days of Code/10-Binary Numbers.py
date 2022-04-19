""" Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!
Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.
Example
The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .
Input Format
A single integer, .
Constraints
Output Format
Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .
Sample Input 1
5
Sample Output 1
1
"""


"start"
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
counter =0
maxc=0
while n > 0:
    if n % 2 == 1:
        counter +=1
        if counter > maxc:
            maxc=counter
    else:
        counter = 0
    n //= 2
print(maxc);
    
#Every odd values, Increment 1


"end"
