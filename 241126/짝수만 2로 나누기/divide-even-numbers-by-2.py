def check_lst(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] =  arr[i] // 2
    return arr




N = int(input())
lst = list(map(int,input().split()))
lst = check_lst(lst)
for i in lst:
    print(i, end=" ")