num = list(map(int,input().split()))

answer = 1
for i in range(1, min(num)):
    if num[0] % i == 0 and num[1] % i == 0:
        answer = i
print(answer)