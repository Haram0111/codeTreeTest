n, m = map(int,input().split())
lst = list(map(int,input().split()))

def sum_lst(a1,a2):
    answer = 0
    for i in range(a1-1, a2):
        answer += lst[i]
    return answer

for i in range(m):
    a1, a2 = map(int,input().split())
    print(sum_lst(a1,a2))
