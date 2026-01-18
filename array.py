
'''from array import*

arr1= (array('i',[0,22,33,12,32,54,56,66]))
for i in arr1:
    print(i)
print(arr1.tolist())

'''

from array import*

# Create an array of integers ('i')
numbers = (array('i', [10, 20, 30, 40,50]))

# 1. Accessing an item (The first item is index 0)
print(numbers[0])  # Output: 10

# 2. Adding an item
numbers.append(50)

# 3. Removing an items
numbers.remove(20)

# 4. Finding the length
print(len(numbers)) # Output: 4
print(numbers.tolist())
for x in numbers:
    print(x)