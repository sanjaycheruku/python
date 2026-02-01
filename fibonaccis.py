def fib(n):
    a=0
    b=1
    if n==0:
        print(a)
    elif n==1:
        print(b)
    else:
        print(a)
        print(b)

    for i in range(2,7):
        c=a+b
        b=c
        a=b
        print(c)
re=fib(5)
print(re)
   
