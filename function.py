

def fun():
    print("happy new year")
print(fun())



def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print("16 is:",evenOdd(16))
print(evenOdd(7))



def fun(name,hello):
    print(f'hello frend {name} yours {hello} ')
fun(name="sanju",hello="mine")



def fruits(eating):
    print(f'i like eating { eating} this thing')
fruits('mango')
fruits('papaay')


def add_numbers(a, b):
    return a + b
result = add_numbers(5, 10)
print(result,result)


def cal(height,weight):
    return height*weight
print(cal(2,3))
print(cal(4,5))


def add_numbers(a, b):
    return a + b
print(add_numbers(5, 10))
print(add_numbers(20, 10))
