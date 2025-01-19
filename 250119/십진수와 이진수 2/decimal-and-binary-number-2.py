N = list(input())
N = N[::-1]
lst = []
number = 0

# Write your code here!
for i in range(len(N)):
    number += int(N[i]) * pow(2,i)
number *= 17

while number >= 2:
    lst.append(number % 2)
    number = number // 2
lst.append(number)

for i in lst[::-1]:
  print(i, end = "")  