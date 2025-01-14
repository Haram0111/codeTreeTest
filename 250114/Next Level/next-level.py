user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Write your code here!
class User:
    def __init__(self, name='codetree', level=10):
        self.name = name
        self.level = level

user = User()
user2 = User(user2_id, user2_level)

print("user", user.name, "lv", user.level)
print("user", user2.name, "lv", user2.level)