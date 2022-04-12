"""Have the function PalindromeTwo(str) take the str string parameter 
being passed and return the string true if the string is palindrome. Otherwise return the string false.
the string may have punctuation but it should not affect.
Input: Noel sees - leon
Output: true """
--start
def PalindromeTwo(strParam): 
  string = strParam
  sa = ''.join([i for i in string if i.isalpha()])
  if sa[::-1].upper() == sa.upper():
    return true
  else:
    return false;
  
  return strParam

--end
