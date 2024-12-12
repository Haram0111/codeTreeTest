def print_start(num):
    if num > 0:
        print_start(num -1)
        print("*" * num)

print_start(5)