"""Given an array of integers and a positive integer k, determine the number of i,j pairs where i < j and ar[i} + ar[j] is divisible by k.
Example
Three pairs meet the criteria:  and .
Function Description
Complete the divisibleSumPairs function in the editor below.
divisibleSumPairs has the following parameter(s):
int n: the length of array 
int ar[n]: an array of integers
int k: the integer divisor
Returns
- int: the number of pairs
"""

"Start"

The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    cnt = 0
    for i in range(len(ar)): 
        for j in range(i + 1, len(ar)):
            tot = (ar[i] + ar[j]) #total value of the 2 array elements
            d = (tot % k ) #divisibilty of the total value of the 2 array elements
            if d == 0:
                cnt +=1
    return cnt;
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


"End"
