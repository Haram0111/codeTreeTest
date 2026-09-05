n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
for i in range(len(grid[0])-3+1):#세로 
    for j in range(len(grid[0])-3+1):#가로
        cnt = 0 
        for k in range(3):
            cnt += grid[i+k][j:j+3].count(1)
        if cnt > answer:
            answer = cnt
print(answer)