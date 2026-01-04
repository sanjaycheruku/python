terms = 5
n1=3
n2=5
count=0
print('fibonacci sequence up to',)
while count <terms:
     print(n1, end=',')
     nth=n1+n2
     n1=n2
     n2=nth
     count+=1
