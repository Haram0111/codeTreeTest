N, B = map(int, input().split())

# Write your code here!
lst = []
while N >= B:
    lst.append(N % B)
    N = N // B
lst.append(N)

for i in lst[::-1]:
    print(i, end = "")