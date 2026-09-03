N = int(input())
lst = list(map(int,input().split(" ")))
numbers = [0] * 9
for i in lst:
    numbers[i-1] += 1
for i in numbers:
    print(i)