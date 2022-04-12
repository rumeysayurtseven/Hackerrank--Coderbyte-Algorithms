"""Task
Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.
Note
In order to get alignment correct, please insert the line  below the numpy import.
Input Format
A single line containing the space separated values of  and .
 denotes the rows.
 denotes the columns.
Output Format
Print the desired X array.
Sample Input
3 3
Sample Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]"""
"start" 
import numpy
numpy.set_printoptions(legacy='1.13')



n, m = map(int, input().split()) # taking number of rows and column
arr = numpy.eye(n,m)
print(arr);

"end"
