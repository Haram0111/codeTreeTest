A, B = input().split(" ")
A, B = int(A), int(B)
answer = 0
dic = {}
while A > 1:
    num = A % B
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1
    A = A // B
    #print(num)
for i in dic.values():
    answer += i ** 2
print(answer)