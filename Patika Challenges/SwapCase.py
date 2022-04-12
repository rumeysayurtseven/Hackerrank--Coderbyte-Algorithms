""" You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description
Complete the swap_case function in the editor below.
swap_case has the following parameters:
string s: the string to modify
Returns
string: the modified string
Input Format
A single line containing a string . """

"start"
def swap_case(s):
    s1 = '';
    for char in (s):
        if (char.islower() == True):
            s1 += (char.upper())
        elif (char.isupper() == True):
            s1 += (char.lower())
        else:
            s1 += char 
    return s1;

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

"end"
