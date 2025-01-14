n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Write your code here!
str.sort(key=lambda x: (not x.startswith(t), x))
print(str[k-1])
