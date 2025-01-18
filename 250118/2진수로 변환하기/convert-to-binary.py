n = int(input())

# Write your code here!
lst = []
while n >= 2:
    lst.append(n % 2)
    n = n // 2
lst.append(n)

for i in lst[::-1]:
    print(i, end = "")