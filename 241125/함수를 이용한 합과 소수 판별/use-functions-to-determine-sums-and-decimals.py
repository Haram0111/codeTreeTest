def check_prime(n):
    for i in range(2, n):
        if n % i == 0: #약수가 존재 = 소수 아님
            return False
    return True

def check_odd(n):
    n = str(n)
    number = 0
    for i in n:
        number += int(i)
    if number % 2 == 0: #합이 짝수임
        return True
    else:
        return False

a, b = map(int,input().split())
answer = 0
for i in range(a,b+1):
    if check_prime(i) and check_odd(i):
        answer += 1
print(answer)