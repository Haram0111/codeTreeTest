def answer(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return answer(n-1) * answer(n-2) % 100

n = int(input())
print(answer(n))