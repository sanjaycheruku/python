import random;

#a=random.randint(0,7)  # we get 0 t0  7 random numbers
#a=random.randrange(1,4)  # we not get 4 as output 1 to 3 we get as output
#   a=random.random();  #it's uses for float 


l=[1,5,3,6,9,5];
a=random.choices(l)

print(a)

'''
print('side')
side=random.randint(0,1)
print(side)
if(side==0):
    print('heads')
else:
    print('tails')
'''