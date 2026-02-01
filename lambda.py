
# map      applies every element
# filter   only matched elements
# reduce    comine all elements



'''
f= lambda a :a* a+22
#res=f(3)
print(f(66))

'''

'''
# maps uses that applies that function to every element
a=(22,33,44,55)
ass=((lambda a:a*10))
print(tuple(map(ass,a)))

'''


'''
# filter every element will satisfy

a=(1,2,3,4,5,6)
eql=lambda a:a%2 != 0
print(*filter(eql,a))

'''


a=(1,2,3,4,5,6)
# map method
print(*map(lambda a:a+2,a))
# filter method
print(*filter(lambda a:a%2==0,a))
# reduce method
from functools import reduce
print(reduce(lambda a,b:a+b,a))
