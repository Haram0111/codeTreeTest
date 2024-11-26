def check_double(_str):
    lst = []
    for i in _str:
        if len(lst) >= 2:
            return "Yes"
        if i not in lst:
            lst.append(i)
    return "No"

_str = input()
print(check_double(_str))