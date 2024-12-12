def print_start(num):
    if num > 0:
        print_start(num -1)
        print("*" * num)

num = int(input())
print_start(num)