""" Have the function ConsonantCount(str) take the str string parameter 
being passed and return the number of consonants the string contains.
Input: Hello World
Output: 7 """

--start
strParam = strParam.replace(" ","")
vowels = 'aeiou'
constant_num = 0
for char in strParam:
  if char not in vowels:
    constant_num +=1
   return constant_num;



--
