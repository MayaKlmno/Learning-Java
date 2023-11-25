# 3.15.23
# Notes comments and Variables 


if 5 > 2:
    print("Five is greater than two!")

#this is a comment
"""
if you want a comment to go in more than just one line this is the easiest way to make it.
"""

# variables
x = "Bonjour"
y = "hello"   # this is a type of string 
z = 8   # this is a type of integer 
print(x)
print(y)
print(x , y, x, y, z)
print(z)

"""
CASTING
- you can do this
- this is something you can do to specify what you want to print out.
here are some examples
"""
a = str(3) # this will print '3'
b = int(3) # this will print 3
c = float(3) # this will print 3.0

"""
GET THE TYPE
If you want to know what type a specific variable is you print this:
"""
print(type(x))
print(type(z))

"""
They types of quotes you use do not really matter for example you an use single or double quotes and you will get the same outcome. 
"""

a = 4
A = "Sally"
# for this A will NOT overwrite a

"""
VARIABLES
Variables can have short names such as x and y, but they can also have longer names such as: 
-again they can be ANYTHING that you want. 
-But what you ahve to have is everything connected. there cannot be any space between them not can they be connected 
by -. but they can be connected by this _. 
-variable names are case-sensative. 
"""
myvar = "Louis"
my_var = "Louis"
_my_var = "Louis"
myVar = "Louis"
MYVAR = "Louis"
myvar2 = "Louis"

"""
usually they are hard to read if they are all next to eachother. but there are some ways to make them easier to read. 
"""

# Camal case
myVariableName = "bagel"

# pascel case
myVariableName = "bagel"

# Snake Case
my_variable_name = "bagel"

"""
Something python also alows you to do is assign mutliple variables in one line
-when doing this you need to make sure that the numbher of variables matches the number of variables. 
    - if you dont do this thne you will get an error. 
"""

x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)

"""
You can assign the same variable to multiple values.
"""

x = y = z = "apples"
print(x)
print(y)
print(z)

"""
you can also unpack the lists so that they can all be in the same line. such as this:
- when you do this the order is important. for this x goes with apple, b goes with banana and z goes with cherry.
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""
if you want to write the code faster to you seperate the varibles by commas. They will be printed out in that order.
they will all be printed out in one line. 
"""

x = "I"
y = "want"
z = "to"
a = "go"
b = "to"
c = "MIT, Oxford, Georgia Tech, or CalTech"
print(x, y, z, a, b, c)

"""if you dont want to have commas in between all of the letters you can replace them with a '+' (plus sign)"""

x = "I"    # x = "I "
y = "want"   # y = "want "
z = "to"     # x = "to "
a = "go"   # a = "go "
b = "to"   # b = "to "
c = "MIT, Oxford, Georgia Tech, or CalTech"  # you don't need a space after this string because it is the last line for this section. 
print(x + y + z + a + b + c)

"""for this you need to have a space after the string if not evreything will be wrote out one after the other"""

"""
when you want to add things the + sign can be used to add two differnt numbers
"""
x = 5
y = 10
print(x + y)

"""
when you want to combine a string and a number, python will say there is an error
"""

"""
if you want to print different variable types such as a string and a number make sure that there is a comma between them. 
"""

x = "bob"
y = 8
print(x, y)


"""
Global variables are variables which are created outside of a function. 

these can be used by evreyone both inside and outside the functions.

How to use it;
    create a variable outside a function, and use it inside the funciton. 

this is a function. 

If you create a variable with the same name inside a function,
this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was,
global and with the origional value. 
"""

x = "awesome"
def myfunc():
    print("Python is" + x)

myfunc()

"""
if you want to create a varibale inside a function, with the same name as the global variable. AN example of the following is 
after this:
"""
x = "awesome"

def myfunc():
    x = "fantastic"
    print("python is" + x)

myfunc()
print("Python is" + x)


# DAY 2  ------- 3.16.23


"""
Usually when you create a variable inside a function that variable is considered: local variable. Meaning that that can only be 
used inside that specific function. If you want that variable, inside the function, to be used all around then you will have to 
assign the "global" value to it such as the next example
"""
def myfunc():
    global x   # this is how you assign a variable the 'global' value. For this the variable x is the global variable. 
    x = "fantastic" # now you can call upon this x in and outside of this fucntion. 

myfunc() # when you open a function you have to close the function... this is how you close it. 

print("Python is" + x)

"""
If you already have a variable with a value... you can use the global keyword to change it. Once you do that evrething
before the keyword will be the first value, but evreything after the keyword will be the next value. 
"""

x = "awesome" # variable x --> value 1

print(x)  # this will print 'awesome'

def myfunc(): 
    global x   # by using the global keyword you create a new value for the same variable. Evrething after this will now
                # be the new value for x
    x = "fantastic"   # you change the variable to another value -->2
myfunc()

print("Python is" + x)   # the sec ond value of x. 

# This is the end of the lesson... for the next lesson go to the next file. :)