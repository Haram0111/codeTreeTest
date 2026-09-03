a, b = map(int,input().split())
lst = [a,b]
for i in range(2,10):
    lst.append(lst[-1] + 2*lst[-2])
for i in lst:
    print(i, end = " ")