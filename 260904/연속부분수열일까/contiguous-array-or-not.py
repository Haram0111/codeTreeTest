N, M = map(int, input().split())

n = list(map(int, input().split()))
m = list(map(int, input().split()))

answer = "No"

for pre in range(N):
    if n[pre] == m[0]:

        answer = "Yes"

        for i in range(M):
            if pre + i >= N:
                answer = "No"
                break

            if n[pre + i] != m[i]:
                answer = "No"
                break

        if answer == "Yes":
            break

print(answer)