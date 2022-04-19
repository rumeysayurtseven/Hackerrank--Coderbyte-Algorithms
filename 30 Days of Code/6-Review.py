""" Objective
Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.
Task
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
Note:  is considered to be an even index.
Example
Print abc def
Input Format
The first line contains an integer,  (the number of test cases).
Each line  of the  subsequent lines contain a string, . """

"start"
N = int(input())
for i in range(0,N):
    string = input()
    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end='')

    print(" ", end='')

    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end='')

    print("")
  


"end"
