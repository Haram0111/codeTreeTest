N = int(input())
lst = list(map(int,input().split(" ")))
ch = [ i ** 2 for i in lst]
for i in range(N):
    print(ch[i], end = " ")