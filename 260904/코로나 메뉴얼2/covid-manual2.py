lst = [0] * 4 #ABCD
for i in range(3):
    a,b = input().split(" ")
    if a == "Y":
        if int(b) >= 37:
            lst[0] += 1
        else:
            lst[2] += 1
    else:
        if int(b) >= 37:
            lst[1] += 1
        else:
            lst[3] += 1
for i in lst:
    print(i, end =" ")
if lst[0] >= 2:
    print("E", end=" ")