# this is jst that user given elements

from array import*

arr = array('i',[])
n= int(input("enter length of array: "))

for i in range (n):
    x=int(input("enter the next number: "))
    arr.append(x)
print(arr)
# from here to find element3
ele=int(input('eneter the number:'))
if ele in arr:
    print(f'element{arr} exist in  my arr')
    
else:
    print(f'ele {arr} don exist')