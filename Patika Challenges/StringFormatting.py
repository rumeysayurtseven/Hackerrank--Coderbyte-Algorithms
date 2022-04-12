""" Given an integer, , print the following values for each integer  from  to :
Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description
Complete the print_formatted function in the editor below.
print_formatted has the following parameters:
int number: the maximum value to print
Sample Input
17
Sample Output
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001 
   """


"start"
def print_formatted(number):
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        a = "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)
        print(a)
    
"""    
binary = "{0:b}".format(n)
Octal = "{0:o}".format(n)
Hexadecimal = "{0:X}".format(n)
"""
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

"end"
