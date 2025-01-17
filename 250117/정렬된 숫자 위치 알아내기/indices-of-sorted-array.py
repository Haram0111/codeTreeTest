n = int(input())
sequence = list(map(int, input().split()))

# Write your code here!
lst_sequence = list((i, [0, sequence[i]]) for i in range(n)) #원래 lst
lst_sequence.sort(key=lambda x : (x[1][1], x[0]))
for i in range(n):
    lst_sequence[i][1][0] = i+1 #몇 번째로 이동했는가
lst_sequence.sort(key=lambda x : x[0])
for i in lst_sequence:
    print(i[1][0], end = " ")