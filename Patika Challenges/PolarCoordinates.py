"""
Sample Input
  1+2j
  
Sample Output
 2.23606797749979 
 1.1071487177940904
"""
"start"
import cmath
z = complex(input())
print(abs(z))
print(cmath.polar(z)[1]);

"end"
