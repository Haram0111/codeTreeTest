N = int(input())
n = list(map(int,input().split(" ")))
count = 0

for i, value in enumerate(n):
    if value == 2:
        count += 1

        if count == 3:
            print(i+1)
            break