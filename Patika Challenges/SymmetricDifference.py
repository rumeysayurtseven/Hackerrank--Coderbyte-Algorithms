""" Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
Input Format
The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.
Output Format
Output the symmetric difference integers in ascending order, one per line.
Sample Input
STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output
5
9
11
12 
"""

"start"
M = int(input())
mset = set(map(int, input().split()))
N = int(input())
nset = set(map(int, input().split()))

mdif = mset.difference(nset)
ndif = nset.difference(mset)

unions=mdif.union(ndif)
for i in sorted(list(unions)):
    print(i)
   

"end"
