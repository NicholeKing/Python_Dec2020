import random
import math

# Basic array
arr1 = [2,3,5,7,8]
print(arr1)
print(f"The first value of this array is: {arr1[0]}")
print(f"The last value of this array is: {arr1[len(arr1)-1]}")

# Nested Arrays
nest_arr = [[1,2], [5,7], [2,5,8]]
print(nest_arr)
print(f"First value in my first array: {nest_arr[0][0]}")
print(f"Second value in the second array: {nest_arr[1][1]}")
# If you know where the last value is:
print(f"Last value in the last array option 1: {nest_arr[2][2]}")
# If you don't know where the last value is:
print(f"Last value in the last array option 2: {nest_arr[-1][-1]}")

# Change all instances of 2 in the nested array to the string "two"
for i in range(len(nest_arr)):
    for j in range(len(nest_arr[i])):
        if nest_arr[i][j] == 2:
            nest_arr[i][j] = "two"
        else: 
            continue

print(nest_arr)

# Dictionaries
teacher = {
    'name': "Nichole",
    'age': 26,
    'hasBrownHair': True,
    'lucky_numbers': [5,7]
}

TA = {
    'name': "Chris",
    'age': 26,
    'hasBrownHair': True,
    'lucky_numbers': [5,7]
}

print(teacher)
print(teacher['name'])
teacher['age'] = 27
print(teacher['age'])
print(teacher['lucky_numbers'])

for key,value in teacher.items():
    print(f"{key}: {value}")

for key,value in TA.items():
    print(f"{key}: {value}")

# Random
print(random.random())
def randInt(min=0, max=100):
    num = random.random() * max
    return math.floor(num)

print(randInt())

arr2 = ["one", "two", "three", "four"]
idx = randInt(max=len(arr2))
print(arr2[idx])

# Print a decimal to the second place
val = 7/9
print("{:.2f}".format(val))