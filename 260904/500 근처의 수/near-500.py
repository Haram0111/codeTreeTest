n = list(map(int,input().split(" ")))
min_num = 9999
max_num = -9999
for i in n:
    if i - 500 >= 0 and i < min_num:
        min_num = i
    elif i - 500 < 0 and i > max_num:
        max_num = i
print(max_num, min_num)