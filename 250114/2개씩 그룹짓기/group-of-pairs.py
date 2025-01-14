n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
nums.sort()
answer = 0
for i in range(n):
    pre = nums[i] + nums[2*n - i - 1] 
    if pre > answer:
        answer = pre
print(answer)