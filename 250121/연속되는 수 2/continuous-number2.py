n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
answer = 0
for i in range(n):
    if arr[i] != arr[i - 1] or i == 0:
        answer += 1
print(answer)