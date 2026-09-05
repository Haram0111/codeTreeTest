N = int(input())
lst = list(map(int,input().split(" ")))

answer = max(lst)
for i in range(len(lst)-1):
    if answer > abs(lst[i] - lst[i+1]):
        answer = abs(lst[i] - lst[i+1])
print(answer)