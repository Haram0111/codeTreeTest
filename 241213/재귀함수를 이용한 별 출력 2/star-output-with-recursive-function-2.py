def print_star(num):
    print("* " * num)
    if num > 1:
        print_star(num - 1)
        print("* " * num)
    elif num == 1:
        print("*")

num = int(input())
print_star(num)