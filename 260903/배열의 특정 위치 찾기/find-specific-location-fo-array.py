lst = list(map(int,input().split(" ")))
# num1 = 0; num2 = 0
# for i in range(10):
#     if i%2 == 1:
#         num1 += lst[i]
#     if i%3 == 2:
#         num2 += lst[i]
# print(num1, f"{num2 // 3:.1f}")

lst1 = lst[1::2]
lst2 = lst[2::3]
print(sum(lst1), round(sum(lst2) / len(lst2), 1))