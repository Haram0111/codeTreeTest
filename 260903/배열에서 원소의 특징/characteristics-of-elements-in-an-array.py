N = list(map(int,input().split(" ")))
for i in range(len(N)):
    if N[i] % 3 == 0:
        print(N[i-1])
        break