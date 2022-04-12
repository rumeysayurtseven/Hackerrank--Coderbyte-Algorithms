"""
Output Format
Output the space separated tuples of the cartesian product.
Sample Input
 1 2
 3 4
 
Sample Output
 (1, 3) (1, 4) (2, 3) (2, 4)
"""

"start"
import itertools

A = set(map(int, input().split()))

B = set(map(int, input().split()))

output =tuple(itertools.product(A,B))
for i in output:
    print(i, end = " ");

"end"
