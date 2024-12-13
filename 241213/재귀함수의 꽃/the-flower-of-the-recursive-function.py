def print_num(num):
    print(num, end=" ")
    if num > 1:
        print_num(num - 1)
        print(num, end=" ")
    elif num == 1:
        print(num, end=" ")

num = int(input())
print_num(num)