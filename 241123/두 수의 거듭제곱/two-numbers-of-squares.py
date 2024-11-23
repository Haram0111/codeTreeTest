def mini(a,b):
    answer = a
    for i in range(b-1):
        answer = answer * a
    return answer

a, b = map(int,input().split())
print(mini(a,b))    