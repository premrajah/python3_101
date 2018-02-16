#
# functions
#

# define basic function
def function1():
    print("I am a function -")

function1()
print(function1())
print(function1)

print("---")

# function that takes arguments
def function2(arg1, arg2):
    print(arg1, " - ", arg2)

# fucntion that returns a value
def cube(x):
    return x*x*x

function2(10, 20)
print(function2(10, 20))
print(cube(3))

print("---")

# function with a default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(2))
print(power(2, 3))
print(power(x=3, num=2))

print("---")

# function with a variable number of arguments 
# variable arg always has to be the last argument
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(4,5,10,4))
print(multi_add(10,4,5,10,4))