def up_scale(n):
    for i in range(1,n+1):
        print(i, end=" ")
    
def down_scale(n):
    for i in range(n,0,-1):
        print(i, end=" ")

n = int(input())
up_scale(n)
print()
down_scale(n)