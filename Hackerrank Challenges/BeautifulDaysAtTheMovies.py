""" Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, 
given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 109.
She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.
Given a range of numbered days,  and a number , determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where i-reverse(i) 
is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Return the number of beautiful days in the range.
Function Description
Complete the beautifulDays function in the editor below.
beautifulDays has the following parameter(s):
int i: the starting day number
int j: the ending day number
int k: the divisor
Returns
int: the number of beautiful days in the range """


"start"

The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    cnt = 0
    for a in range(i,j+1):
        rn = (str(a)[::-1])
        if abs(a-int(rn)) % k == 0:
            cnt +=1
            
    return cnt;
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()


"end"
