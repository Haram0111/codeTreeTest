n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort(reverse=True)
answer = -1
for i in nums:
    if nums.count(i) >= 2:
        continue
    else:
        answer = i
        break
print(answer)