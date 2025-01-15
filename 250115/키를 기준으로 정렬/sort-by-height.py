n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Write your code here!
class User:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    
lst_user = [User(name[i], height[i],weight[i]) for i in range(n)]
lst_user.sort(key=lambda x : x.height)
for i in range(n):
    print(lst_user[i].name, lst_user[i].height, lst_user[i].weight)
