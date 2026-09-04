n = int(input())
a = list(map(int, input().split()))
answer = []
# Please write your code here.
num = len(a)+1
while num != 0:
    num = a[:num].index(max(a[:num]))
    #print(num)
    answer.append(num+1)
for i in answer:
    print(i, end = " ")