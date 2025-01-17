a, b, c = map(int, input().split())
origin_time = (11 * 24 + 11) * 60 + 11
check_time = (a*24 + b) * 60 + c
# Write your code here!
answer = 0
if check_time < origin_time:
    print(-1)
else:
    print(check_time-origin_time)