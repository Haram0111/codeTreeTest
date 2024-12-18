def print_sum(n):
    if n < 10:
        return n
    return print_sum(n // 10) + (n % 10)

lst = list(map(int,input().split()))
answer = print_sum(lst[0] * lst[1] * lst[2])
print(answer)