Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format.


--start

def timeConversion(s):
    a= ''
    # Checking if last two elements of time
    # is AM and first two elements are 12
    # remove the AM 
    if s[-2:] == "AM" :
      if s[:2] == '12':
          a = str('00' + s[2:8])
      else:
          a = s[:-2]
   
    # Checking if last two elements of time
    # is PM and first two elements are 12 
    else:
      if s[:2] == '12':
          a = s[:-2]
      else:
          a = str(int(s[:2]) + 12) + s[2:8]
    return a      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


--end
