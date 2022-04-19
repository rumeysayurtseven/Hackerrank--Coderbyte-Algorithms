""" Today, we will learn about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video.
Task
Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.
Example
Print 4 3 2 1. Each integer is separated by one space.
Input Format
The first line contains an integer,  (the size of our array).
The second line contains  space-separated integers that describe array 's elements.
Constraints
Constraints
, where  is the  integer in the array.
Output Format
Print the elements of array  in reverse order as a single line of space-separated numbers. """

"start"
import math
import os
import random
import re
import sys    


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    revarr= arr[::-1] #reverse of the array
    listToStr = ' '.join(map(str, revarr))
    print(listToStr);

"end"
