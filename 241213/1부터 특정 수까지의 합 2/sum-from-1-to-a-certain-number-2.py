def all_sum(num):
    if num == 1:
        return 1

    return all_sum(num - 1) + num

num = int(input())
print(all_sum(num))