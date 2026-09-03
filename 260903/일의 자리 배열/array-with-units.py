a, b = map(int,input().split())
answer = [a,b]
for i in range(2,10):
    answer.append( (answer[i-1] + answer[i-2]) % 10 )
for i in answer:
    print(i, end = " ")