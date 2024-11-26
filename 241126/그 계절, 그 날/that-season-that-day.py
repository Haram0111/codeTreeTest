def check_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True 
            else:
                return False
        return True
    return False

def check_season(m):
    if 3 <= m <= 5:
        print("Spring")
    elif 6 <= m <= 8:
        print("Summer")
    elif 9 <= m <= 11:
        print("Fall")
    else:
        print("Winter")

def check_date(y, m, d): 
    date_lst = [31,28,31,30,31,30,31,31,30,31,30,31]
    if check_year(y): #윤년
        date_lst[1] = 29
    if date_lst[m-1] >= d:
        check_season(m)
    else:
        print("-1")

y, m, d = map(int,input().split())
check_date(y,m,d)