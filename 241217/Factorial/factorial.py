def factorial(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return factorial(n - 1) * n

n = int(input())
print(factorial(n))