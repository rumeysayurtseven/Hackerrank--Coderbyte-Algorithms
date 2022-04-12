""" Task
You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.
Input Format
The first line contains the space separated values of  and .
The next  lines contains the space separated elements of  columns.
Output Format
First, print the transpose array and then print the flatten.
Sample Input
2 2
1 2
3 4
Sample Output
[[1 3]
 [2 4]]
[1 2 3 4] """

"start"
import numpy



n, m = map(int, input().split()) # taking number of rows and column
array = numpy.array([input().strip().split() for _ in range(n)], int)
tarr= numpy.transpose(array)
farr= array.flatten()
print(tarr)
print(farr);

"end"
