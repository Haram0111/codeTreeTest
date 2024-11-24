a, o, c = input().split()
a = int(a)
c = int(c)

def check(a,o,c):
    answer = 0
    if o == '*':
        answer = a * c
        print(a,o,c,"=", answer)
    elif o == '/':
        answer = a // c
        print(a,o,c,"=", answer)
    elif o == '+':
        answer = a + c
        print(a,o,c,"=", answer)
    elif o == '-':
        answer = a - c
        print(a,o,c,"=", answer)
    else:
        print("False")

check(a,o,c)