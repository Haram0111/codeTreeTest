n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Write your code here!
class Student:
    def __init__(self,name,korean,english,math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

lst_student = [Student(name[i], korean[i], english[i], math[i]) for i in range(n)]
lst_student.sort(key=lambda x : (x.korean, x.english, x.math), reverse=True)
for i in lst_student:
    print(i.name, i.korean, i.english, i.math)