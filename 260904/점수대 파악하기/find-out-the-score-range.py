n = list(map(int,input().split(" ")))
lst = [0 for i in range(10)]

for i in n:
    if i == 0:
        break
    if i < 10:
        continue
    lst[i // 10 -1] += 1

for i in range( len(lst)-1, -1, -1 ):
    print((i+1)*10,"-", lst[i] )