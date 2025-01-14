secret_code, meeting_point, time = input().split()
time = int(time)

# Write your code here!
class User:
    def __init__ (self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

user = User(secret_code, meeting_point, time)
print("secret code :", user.secret_code)
print("meeting point :", user.meeting_point)
print("time :", user.time)