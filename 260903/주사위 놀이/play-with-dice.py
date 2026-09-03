lst = [0] * 6
N = list(map(int,input().split(" ")))
for i in N:
    lst[i-1] += 1
for i in range(len(lst)):
    print(i+1,"-", lst[i])