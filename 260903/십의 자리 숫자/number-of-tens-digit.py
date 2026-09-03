N = list(map(int,input().split(" ")))
lst = [0] * 9
for i in N:
    if i == 0:
        break
    if i // 10 >= 1:
        lst[i // 10 - 1] += 1
for i in range(len(lst)):
    print(i+1,"-",lst[i])