N = int(input())
lst = [1, N]
while lst[-1] <= 100:
    lst.append(lst[-1] + lst[-2])
for i in lst:
    print(i, end = " ")