n = int(input())
arr = [int(input()) for _ in range(n)]

# 초기값 설정
answer = 1  # 첫 번째 숫자부터 시작하므로 최소 1번 연속이 있을 것이다.
pre = 1

for i in range(1, n):
    if arr[i-1] == arr[i]:  # 연속된 동일 숫자
        pre += 1
    else:  # 연속이 끊어짐
        answer = max(answer, pre)  # 최대값을 갱신
        pre = 1  # 연속 횟수 초기화

# 마지막 연속 횟수 처리
answer = max(answer, pre)

print(answer)
