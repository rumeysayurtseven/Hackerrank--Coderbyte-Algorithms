"""Have the function PrimeTime(num) take the str string parameter 
being passed and return true if parameter is prime, otherwise return the string false. The range will be between 
1 ans 2^16. 
Input: 19
Output: true  """
--start

def PrimeTime(num):
  if num <=1:
    return false
  elif num == 2:
    return true
 for i in range(2,num):
  if num % i = 0:
    return false
 return true;
