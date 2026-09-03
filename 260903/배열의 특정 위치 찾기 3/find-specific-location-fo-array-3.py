n = list(map(int,input().split(" ")))
n1 = n.index(0)
print(n[n1-1] + n[n1-2] + n[n1-3])