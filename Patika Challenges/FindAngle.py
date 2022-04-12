"""
Sample Input
10
10
Sample Output
45°
"""

"start"
import math

ablen= int(input())
bclen = int(input())

H = math.sqrt((ablen**2) + (bclen**2))
H = H / 2.0
bc = bclen / 2.0

angle = int(round(math.degrees(math.acos(bc/H))))
angle = str(angle)
degree_sign = u"\N{DEGREE SIGN}"

print(angle + degree_sign)
        

"end"
