m1, d1, m2, d2 = map(int, input().split())
A = input()

# Write your code here!
date = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
date1 = 0
date2 = 0
for i in range(m1):
    date1 += month[i]
date1 += d1

for i in range(m2):
    date2 += month[i]
date2 += d2
A_index = date.index(A)
print((date2 - date1 - A_index) // 7 + 1)