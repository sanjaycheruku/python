user_list = []
num_elements = int(input("How many elements do you want to enter? "))

for i in range(num_elements):
    value = input(f"Enter element {i+1}: ")
    # Append the value to the list (can convert to int/float if needed)
    user_list.append(value)

print("The user array is:", user_list)
