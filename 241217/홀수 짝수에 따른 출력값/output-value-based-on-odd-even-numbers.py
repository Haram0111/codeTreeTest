def print_all(n,ans):
    if n < 2:
        return ans + n
    if n % 2 == 0: #짝수
        return print_all(n - 2, ans + n)
    else: #홀수
        return print_all(n - 2, ans + n)

n = int(input())
print(print_all(n,0))