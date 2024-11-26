def check_double(_str):
    lst = []
    for i in _str:
        if i not in lst:
            lst.append(i)
        if len(lst) >= 2:
            return "Yes"
    return "No"

_str = input()
print(check_double(_str))