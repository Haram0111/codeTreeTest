def print_line(n,m):
    for j in range(n):
        for i in range(m):
            print("1", end="")
        print()

n, m = map(int,input().split())
print_line(n,m)
