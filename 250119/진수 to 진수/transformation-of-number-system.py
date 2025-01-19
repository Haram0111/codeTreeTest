a, b = map(int, input().split())
n = list(input())

n = n[::-1]
lst = []
# Write your code here!
number = 0
for i in range(len(n)):
    number += int(n[i]) * pow(a,i)

while number >= b:
    lst.append(number % b)
    number = number // b
lst.append(number)

for i in lst[::-1]:
    print(i, end="")

