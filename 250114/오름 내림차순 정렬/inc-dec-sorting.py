n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
nums.sort()
for i in nums:
    print(i, end=" ")
print("")
nums.sort(reverse=True)
for i in nums:
    print(i, end=" ")
