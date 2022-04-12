"""
Input Format
The first line contains . The second line contains an array   of  integers each separated by a space.
Print the runner-up score.
Sample Input 0
5
2 3 6 6 5
Sample Output 0
5
"""


"start"
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])
"end"
