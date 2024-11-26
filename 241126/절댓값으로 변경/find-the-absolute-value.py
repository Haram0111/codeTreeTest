def absolute_value(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    return arr

N = int(input())
lst = list(map(int,input().split()))
lst = absolute_value(lst)
for i in lst:
    print(i, end=" ")