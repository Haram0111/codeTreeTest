n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Write your code here!!
class Student:
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

lst_sutdent= [Student(students[i][0], students[i][1], i+1) for i in range(n)]
lst_sutdent.sort(key=lambda x : (-x.height, -x.weight))

for i in lst_sutdent:
    print(i.height, i.weight, i.idx)
