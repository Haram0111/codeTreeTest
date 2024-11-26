def is_valid_palindrome(_str):
    for i in range(len(_str)//2):
        if _str[i] != _str[len(_str) -i -1]:
            return "No"
    return "Yes"

_str = input()
print(is_valid_palindrome(_str))