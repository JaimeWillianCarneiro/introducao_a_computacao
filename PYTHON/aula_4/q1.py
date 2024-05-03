for num in range(2000, 3201):
    if num%7 ==0 and num%5 !=0:
        if not num +7 > 3200:
            print(num, end=",")
        else:
            print(num)
