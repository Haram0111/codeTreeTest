def trail(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return trail(int(num/3)) + trail(num-1)


num = int(input())
print(trail(num))