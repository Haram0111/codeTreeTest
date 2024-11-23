def prime(n):
    if n == 1:
        return 0
    for i in range(2,n):
        if n % i == 0: #약수 존재
            return 0
    return n

a, b = map(int,input().split())
answer = 0
for i in range(a, b+1):
    answer += prime(i)
print(answer)