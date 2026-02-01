def max(n):
   
    for i in range(0,n+1):
      print('hello',i)
      max(n)
   
n=int(input('eneter no:'))
max(n)