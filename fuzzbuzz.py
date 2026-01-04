for num in range(1,16):
    if num%3==0 and num%5==0:
        print('bye')
    elif num%3==0:
        print('hi')
    elif num%5==0:
        print('ok')
    else:
        print(num)