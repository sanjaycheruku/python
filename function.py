'''
block of code
'''
'''
def func(a,b,c):#function definition
    print("work is function",a,b,c)#function body
    print('max')
func(1,2,3)#function call
'''
'''
#single parameter multi argmeters
def func(*a):#function definition
    print("work is function",a)#function body
    print('max')
func(1,2,3)#function call
'''
'''
#dicnory type
def fc(**a):#function definition
    print("work is function",a)#function body
    print('max')
fc(m=3,n=2)#function call
'''
def max():
    print('win')
    def min():
        print('lose')
    min()
max()