N = list(map(int,input().split(" ")))
print(abs(sum(N[::2]) - sum(N[1::2])))