def function(n, ans):
    if n == 1:
        return ans
    if n % 2 == 0:
       return function(n // 2, ans+1)
    else:
        return function(n * 3 + 1, ans+1)

n = int(input())
print(function(n, 0))

# 3 0
# 10 1
# 5 2
# 16 3
# 8 4
# 4 5
# 2 6
# 1 7