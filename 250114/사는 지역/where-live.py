n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Write your code here!
class User:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

lst_user = [User(name[i], street_address[i], region[i]) for i in range(n)]
lst_user.sort(key=lambda user: user.name)
print("name", lst_user[-1].name)
print("addr", lst_user[-1].address)
print("city", lst_user[-1].city)