n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort(reverse=True)
have = False
for i in nums:
    if nums.count(i) >= 2:
        continue
    else:
        print(i)
        have = True
        break
if have != True:
    print(-1)