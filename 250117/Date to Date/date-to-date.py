m1, d1, m2, d2 = map(int, input().split())

# Write your code here!
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer = 0
for i in range(m1+1, m2):
    answer += num_of_days[i]
answer += d2
answer += (num_of_days[m1] - d1 + 1)
print(answer)