n = int(input())
price = list(map(int, input().split()))

answer = 0
# Please write your code here.
for i in range(len(price)-1):
    if answer < max(price[i+1:]) - price[i]:
        answer = max(price[i+1:]) - price[i]
print(answer)