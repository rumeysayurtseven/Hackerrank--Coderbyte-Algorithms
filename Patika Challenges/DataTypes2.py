""" Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
Example
The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:
alpha
beta
Input Format
The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.
Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0
Berry
Harry """

"start"
if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([score,name])
        # Sort list in Ascending order
    student.sort()
        # Assign the first score to a list which will be the minimum
    grade = student[0][0]
     # Loop through the list by excluding first item in the list and find the second lowest
    for i in range(1,len(student)):
        if grade < student[i][0]:
            grade = student[i][0]
            break
    
    # Loop through the list and print names based on the second lowest score
    for i in range(1,len(student)):
        if student[i][0] == grade:
            print(student[i][1])
        

"end"
