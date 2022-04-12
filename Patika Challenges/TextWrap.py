""" Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

"start"
import textwrap


def wrap(string, max_width):
    
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
"end"
