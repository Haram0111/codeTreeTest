n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Write your code here!
# print(points[0][1][0])
# print(points[0][1][1])
points.sort(key=lambda x : (abs(x[1][0]) + abs(x[1][1]), x[0]))
for i in points:
    print(i[0] + 1)