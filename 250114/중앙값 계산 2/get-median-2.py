n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
lst = []
for i in range(n):
    lst.append(arr[i])
    if len(lst) % 2 == 1:
        lst.sort()
        print(lst[len(lst)//2], end = " ")