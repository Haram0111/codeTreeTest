a,b = map(int,input().split(" "))
lst = list(map(int,input().split(" ")))
for i in range(b):
    tmp = list(map(int,input().split(" ")))
    if tmp[0] == 1:
        print(lst[tmp[1]-1])
    elif tmp[0] == 2:
        if tmp[1] in lst:
            print(lst.index(tmp[1])+1)
        else:
            print(0)
    else:
        for j in range(tmp[1]-1, tmp[2]):
            print(lst[j], end=" ")
        print()