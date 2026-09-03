lst = list(map(int,input().split(" ")))
for i in range(lst.index(0)):
    if lst[i] % 2 != 0:
        lst[i] += 3
    else:
        lst[i] = lst[i] // 2
    print(lst[i], end = " ")