# 3.16.23

# This Lesson is about Data Types

"""
DIFFERNT DATA TYPES:

Text Type: str    
Numeric Types: int, float, complex
Sequence Types: listy, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearry, memoryview
None Type: NoneType
""" 

"""
If you want the compter to tell you what data type a variable is you can do this:
"""

x = 5
print(type(x))


"""
str  ---> x = "Hello World"
int --->  x = 30
float ---> x = 30.5
complex ---> x = 1j
list ---> x = ["apple", "banana", "cherry"]  !!! notice that the difference between this and the next one is the type of [] or ()
tuple ---> x = ("apple", "banana", "cherry")
range --> x = range(6)
dict ---> x = {"name" : "John", "age" : 36}
set ---> x = {"apple", "banana", "cherry"}
forozenset ---> x = frozenset({"apple", "banana", "cherry"})
bool ---> x = True
bytes ---> x = b"Hello"
bytearray ---> x = bytearray(5)
memoryview ---> x = memoryview(bytes(5))
NoneType ---> x = None
"""

"""
x = str("Hello World") ---> str
x = int(20) ---> int
x = float(20.5) ---> float
x = complex(1j) ---> complex
x = list(("apple", "banana", "cherry")) ---> list
x = tuple(("apple", "banana" , "cherry")) ---> tuple
x = range(6) ---> range
x = dict(name="John", age=36) ---> dict
x = set(("apple", "banana", "cherry")) ---> set
x = frozenset(("apple", "banana", "cherry")) ---> frozenset
x = bool(5) ---> bool
x = bytes(5) ---> bytes
x = bytearray(5) ---> bytearray
x = memoryview(bytes(5)) ---> memoryview
"""

# Numbers

# 3.17.23

"""
There are lots of data types in python. The three numeric types include: int, float, and complex. 
"""

x = 1    # this is an example of an int data type
y = 2.8  # this is an example of a float data type
z = 1j   # this is an example of a complex data type. 

"""
if you want to check/find out what data type something is you can do this:
"""

print(type(x))
print(type(y))
print(type(z))

# int --> a whole number, positive, or negative, without decimals, of unlimited length

a = 4274973948083840043884
b = 8
c = -13859049023450

# if you check to see what data type they are you can see that they are all int

print(type(a))
print(type(b))
print(type(c))

# float --> a number, positive or negative, conatining at least one decimal

d = 1.0
e = 1.0803949938983098904
f = -1.80394899

print(type(d))
print(type(e))
print(type(f))

# floats can also be scientific numbers with an "e" to indciate the power of 10.

g = 35e3
h = 12E4
i = -87.7e100

print(type(g))
print(type(h))
print(type(i))

# complex --> are written with a "j" as the imaginary part

j = 3+5j
k = 5j
l = -5j

print(type(j))
print(type(k))
print(type(l))
# as you can see these are all complex data types

# you can change from differnt data types

m = 1    # int
n = 2.8  # float
o = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
# BUT you cannot turn complex data types into differnt data types. 

# RANDOM NUMBERS

"""
Python does not have a 'random()' function. but python has a built in random module that can be used
to make random numbers.

This is how you use the random module to choose a random number from 1-9
"""
import random # you have to import this

print(random.randrange(1,10))


# Specify a Varibale Type

"""
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string
        literal (providing the string represents a whole number)
        
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents
a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals.

"""
