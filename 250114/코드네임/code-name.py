MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Write your code here!
class User:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

users = [User(codenames[i], scores[i]) for i in range(MAX_N)]

# Find the user with the minimum score
min_user = min(users, key=lambda user: user.score)

print(min_user.codename, min_user.score)
