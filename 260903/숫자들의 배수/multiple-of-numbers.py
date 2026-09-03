n = int(input())
cnt = 0
num = 1
while cnt < 2:
    print(n*num, end = " ")
    if n*num % 5 == 0:
        cnt += 1
    num += 1