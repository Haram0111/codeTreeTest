def number(n):
    num = 0
    for i in range(n):
        for j in range(n):
            print(number_lst[num], end=" ") # 넘버 바꾸기
            num += 1
            if num == 9:
                num = 0
        print() #줄 바꿈

number_lst = [1,2,3,4,5,6,7,8,9]
n = int(input())
number(n)