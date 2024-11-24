a, o, c = input().split()
a = int(a)
c = int(c)

def check(a,o,c):
    answer = 0
    if o == '*':
        answer = a * c
    elif o == '/':
        answer = a // c
    elif o == '+':
        answer = a + c
    elif o == '-':
        answer = a - c
    else:
        print("False")
    print(a,o,c,"=", answer)

check(a,o,c)