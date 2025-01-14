from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_array(nums, n):
    if n == 1:
        return nums[0]
    return lcm(nums[n - 1], lcm_array(nums, n - 1))

# Input
n = int(input())  # Number of elements
nums = list(map(int, input().split()))  # List of numbers

# Calculate LCM
result = lcm_array(nums, n)
print(result)