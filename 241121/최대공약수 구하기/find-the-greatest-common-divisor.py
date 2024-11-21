num = list(map(int,input().split()))

def find(n,m):
    answer = 1
    for i in range(1, min(num)):
        if num[0] % i == 0 and num[1] % i == 0:
            answer = i
    print(answer)

find(num[0], num[1])