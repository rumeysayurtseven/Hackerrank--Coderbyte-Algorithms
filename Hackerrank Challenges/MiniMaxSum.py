nes (23 sloc)  747 Bytes
  
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

--start
def miniMaxSum(arr):
    mins=0 #minimum sum at first
    maxs=0
    fsum = 0
    max = arr[0]
    min = arr[1]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
        fsum += arr[i]
    mins = fsum - max
    maxs = fsum - min
    print(mins,maxs);
        
        
    
    # Write your code here
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


--end
