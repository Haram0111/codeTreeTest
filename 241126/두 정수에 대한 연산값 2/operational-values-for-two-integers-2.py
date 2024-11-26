def puls(a,b):
    if a > b:
        a *= 2
        b += 10
    else:
        b *= 2
        a += 10
    return a,b

a, b = map(int,input().split())
a, b = puls(a,b)
print(a, b)