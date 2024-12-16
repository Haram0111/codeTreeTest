def finaldivision(n, ans):
    if n == 1:
        return print(ans)
    if n % 2 == 0:
        return finaldivision(n // 2, ans + 1)
    else:
        return finaldivision(n // 3, ans + 1)

n = int(input())
finaldivision(n, 0)