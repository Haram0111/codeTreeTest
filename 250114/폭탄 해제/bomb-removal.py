unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Write your code here!
class User:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

user = User(unlock_code, wire_color, seconds)

print("code :", user.code)
print("color :", user.color)
print("second :", user.second)