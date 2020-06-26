
# Python Syntax
#variable names can be upper or lower
#var names cannot start with numbers
# commands like print must be exactly as defined

# Python Comments
# this is a comment, it is a line of code that will not be executed

# everything after the hashtag is ignored

'''
Using triple single quotes
is a way of doing a multiline comments
though technichally its a 
multiline string that is not run by python
'''
"""
comment also
"""

# Shell vs python file 

# Variables
# python variables are untyped
# a is our variable here
a = 1
# variables can be updated
a = 2
# variables can be assiged to other vars
b = a
#print(b)
#print(a) # the print statements with a # are commented out 
# variables can also be functions
c = lambda x: x+1
#print(c(2))
# variables have naming conventions
this_is_a_caterpillar_name_variable = 1
thisIsACamelCaseVar = 2
ALL_CAPS_VARS_ARE_COMMON_FOR_GLOBAL_VARS = 1354

# Basic Types and operators
# ints or integer
a = 1
b = 2
c = -11123123
# integers can be as big you want
a = 100000 ** 10000
#print(a)
d = 0

# floats
a = 1.0
b = 1.0129384857
c = -1.234234

#booleans
a = True
b = False

# strings
a = "useful strings"
b = "f"
#print(a)
# there are unicode strings 

# Basic Operators
# math
c = 1 + 1
b = 3*3
d = 5/3
e = 3**4
# use brackets to enforce precedence
f = (3-3)*4
#print(f)

# ints are converted to floats
g = 4 + 3.5
#print(g)

# False and True are implicitely 0 and 1
h = False + 1 # converted to 0 + 1
i = True + 1
#print(i)

# strings can be added
a = "gotcha" + " " + "tongue"
#print(a)

# False and True are a basic boolean types

# we can determine the types of our basic or other variables
a = False
b = 1

#print(type(a))
#print(type(b))
true = False
#print(true)

# 'is' is a keyword to compare types of variables
a = False
print(a is bool) # this is incorrect, aka is comparing False is bool
print(type(a) is bool)

# % is modulus aka remainder
a = 9 % 4 # what is the remainder of 9 / 4
#print(a)

# Boolean Logic
# expressions that evaluate to True or False
# True + True + True is not boolean logic, it 
a = True and False
b = True or False
c = 1 <= 10
d = 3 >= 10
e = 4 > 10
f = 5 < 10
g = 4 == 2 + 2
h = (5 == 2+3) == False
print(h)
# integers above 0 are considered True
t = 3 == False
# non empty strings are not true
print(t)
t = 'were' == True 
g = 'true' == True
# string comparisons are common
a = "hi" < "abacus" # strings are compared based on alphabetic order
print(a)

# Strings
# string length
a = "a string"
length_of_a = len(a)
print(length_of_a)
# get a single character of a string
first_char = a[0]
print(first_char)
first_3_letters = a[:3] # this is slicing syntax
print(first_3_letters)
first_3_letters = a[0:3] # we are slicing from index 0 inclusive to 3 exclusive

# Functions
# Tuples, Set, Lists, Dictionaries
# Loops





