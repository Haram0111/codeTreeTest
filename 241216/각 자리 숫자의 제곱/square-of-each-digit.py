def sumofsquare(n):
    num = n % 10
    if n < 10:
        return n * n
    return sumofsquare(n // 10) + num * num

n = int(input())
print(sumofsquare(n))