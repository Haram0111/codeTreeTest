n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Write your code here!
class Student:
    def __init__ (self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
lst_student = [Student(name[i], height[i], weight[i]) for i in range(len(name))]
lst_student.sort(key=lambda x : x.name)
print("name")
for i in lst_student:
    print(i.name, i.height, i.weight)
print("")
print("height")
lst_student.sort(key=lambda x : -x.height)
for i in lst_student:
    print(i.name, i.height, i.weight)
