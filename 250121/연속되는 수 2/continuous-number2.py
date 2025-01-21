n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
answer = 0
pre = 0
for i in range(n):
    #print(pre)
    if i == 0 or arr[i-1] == arr[i]:
        pre += 1
    else:
        if pre > answer:
            answer = pre
            pre = 1
if pre > answer:
    answer = pre
print(answer)