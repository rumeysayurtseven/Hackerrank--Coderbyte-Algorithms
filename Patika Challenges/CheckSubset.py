""" 
You are given two sets,  and .
Your job is to find whether set  is a subset of set .
If set  is subset of set , print True.
If set  is not a subset of set , print False.
Sample Input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output:
True 
False
False
"""
"start"
T = int(input())


for _ in range(T):
    lenA = int(input())
    A = set(map(int,input().split()))
    lenB = int(input())
    B = set(map(int,input().split()))
    print(A.issubset(B)) 


"end"
