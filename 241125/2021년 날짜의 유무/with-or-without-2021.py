def check_date(M, D):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if M < 1 or M > 12:
        return "No"

    if D >= 1 and D <= days_in_month[M - 1]:
        return "Yes"
    else:
        return "No"

M, D = map(int, input().split())
print(check_date(M, D))