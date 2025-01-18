m1, d1, m2, d2 = map(int, input().split())

date = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# Write your code here!
date1 = 0
date2 = 0

for i in range(m1):
    date1 += month[i]
date1 += d1

for i in range(m2):
    date2 += month[i]
date2 += d2

if date1 <= date2: #date2가 더 나중
    print(date[(date2 - date1) % 7])
else: #date1이 더 빠름
    print(date[7- (date1 - date2) % 7])