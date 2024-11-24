a, o, c = input().split()
a = int(a)
c = int(c)
answer = 0
if o == '*':
    answer = a * c
elif o == '/':
    answer = a // c
elif o == '+':
    answer = a + c
elif o == '-':
    answer = a - c
print(a,o,c,"=", answer)