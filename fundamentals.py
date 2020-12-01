# imports a poem
import this
# Opens a browser to a comic
import antigravity

# In JavaScript we declared variables with keywords at the front, ex:
# var number = 0, let i = 1, const num = 19
# In Python, we no longer need var/let/const, you can just declare the variable name
number = 0
i = 1
num = 19

# We can even declare multiple variables and their values at once!
a, b = 1, 2
# And reassign them at once too
b, a = a, b

print(a)
print(b)

# ARRAYS (LISTS)
# arrays -> lists (mostly an interchangeable term here)
mylist = [1,2,3,4,55,6]

# Prints the array
print(mylist)

# FUNCTIONS IN PYTHON
# In JS we made a function like so:
# function add(num1, num2) { 
#   //did something 
# }
# In Python:
def add(num1, num2):
    return num1 + num2

# Notice the use of def instead of function
print(add(2,4))
# Note that printing the function works because of the presence of a return statement in the function

# FOR LOOPS
# There are several ways we can specify what we want from a for loop
# Option 1:
# Be specific about a start, end, and increment amount
for i in range(1,10,2):
    print(i)
# This will print 1, 3, 5, 7, 9

# Option 2:
# Just specify the end point -- it assumes we start at 0 and increment by 1 (based on standard arrays which start at 0 and increment up by 1)
for i in range(3):
    print(i)
# This will print 0, 1, 2

# Option 3:
# Loop with index -- this will run from 0 to the length of your list (remember that the end number provided in non-inclusive, so we won't get an index out of range error)
for i in range(len(mylist)):
    print(mylist[i])

# Option 4:
# Loop through the list and get the value directly
for i in mylist:
    print(i)
# This will print 1,2,3,4,55,6

# WHILE LOOPS
# Use a for loop when you know how long the loop is
# Use a while loop when you don't know how long the loop should run

isrunning = True
count = 0
while isrunning:
    count = count + 1
    if count == 10:
        isrunning = False
    else:
        print("I'm running")

# Careful! This will create an infinite loop!
while True:
    print("this is running")
# Hit ctrl + c (cmd + c on a Mac) to stop the loop in your terminal