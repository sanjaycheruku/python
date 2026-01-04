year=2005
if (year % 4)== 0:
    if (year % 100)== 0:
        if (year % 400)== 0:
            print('year is leap')
else:
    print("year is not leap")