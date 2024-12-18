def function(n, ans):
    if n == 1:
        return ans
    if n % 2 == 0:
       return function(n // 2, ans+1)
    else:
        return function(n * 3 + 1, ans+1)

n = int(input())
print(function(n, 0))