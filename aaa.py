'''
num=6
max=5
for i in range (1, 11):
    print(num,'x',i,"=",num*i)
    print(max,'x',i,"=",max*i)

'''
'''
def ad(x,y):
    z=x+y
    
    return z
a=ad(4,5)

print(a)

'''

'''

def teach():
    print("name:pavan")
    print('age:20.5')
    print('sal:20')
teach()

'''

'''


def teac(p,t,r):
    return (p*t*r)/100
a=teac(1000,2,5)
print('answer:',a)

'''


'''
def sid(side):
    area=side*side
    return area
a=sid(5)
print('area:',a)

'''

'''

def rect(l,b):
    area= 0.5*l*b
    return area
a=rect(4,5)
print("area:",a)

'''

'''
def cir(r):
    area=3.14*r*r
    return area
a=cir(5)
print("area:",a)

'''

'''

def slice(x):
    b=x[::-1]
    print(b)
    return x[:-4:-1]

a=slice('pavan_kumar')
print(a)


'''

'''

def sli(str1,str2):
    a=str1+' '+str2
    b=a[::-1]
    return b
c=sli('pavan','kumar')
print(c)

'''

'''

# Function Definition
def slice_list(lst):
    print("Length of the list:", len(lst))

# Function Call
numbers = slice_list([10, 20, 30, 40, 50])
slice_list(numbers)


'''

def func(name,*email,**address):
    print("Name:", name)
    print("Email:", email)
    print("Address:", address)
func("Pavan", "pavan@example.com","avg@gmail.com" ,city ="Hyderabad", pincode="TS")