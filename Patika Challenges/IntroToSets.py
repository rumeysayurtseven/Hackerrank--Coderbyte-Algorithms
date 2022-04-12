""" Task
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average
of all the plants with distinct heights in her greenhouse.
Function Description
Complete the average function in the editor below.
average has the following parameters:
int arr: an array of integers
Returns
float: the resulting float value rounded to 3 places after the decimal """

"start"

def average(array):
    sumarr= sum(set(array))
    lenarr = len(set(array))
    avgarr= sumarr/lenarr
    return round(avgarr,3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

"end"
