def pibonachi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return pibonachi(n - 1) + pibonachi(n - 2)

n = int(input())
print(pibonachi(n))