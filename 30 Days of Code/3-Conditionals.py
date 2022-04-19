"""Objective
In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.
Task
Given an integer, , perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not n is weird. """

"start"

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

            
if N % 2 != 0:
    print("Weird")
else:
    if N <= 5:
        print("Not Weird")
    elif N <= 20:
        print("Weird")
    else:
        print("Not Weird");
        

"end"
