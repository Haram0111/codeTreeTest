def check_continuous_partial_sequence(origin, check, len1, len2):
    for i in range(len1):
        if i + len2 <= len1:
            if origin[i:i+len2] == check[:len2]:
                return "Yes"
    return "No"


len1, len2 = map(int,input().split())
n1 = list(map(int,input().split()))
n2 = list(map(int,input().split()))
print(check_continuous_partial_sequence(n1, n2, len1, len2))