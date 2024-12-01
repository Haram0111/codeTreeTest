n, m = map(int,input().split())
lst = list(map(int,input().split()))

def all_sum(m):
    answer = 0
    while m >= 1:
        answer += lst[m-1]
        if m % 2 == 0:
            m = m // 2
        else:
            m -= 1
    return answer

print(all_sum(m))