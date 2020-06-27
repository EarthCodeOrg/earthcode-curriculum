# This Module Covers Fundamental Python 

# Python Syntax
# variable (or var) names can be upper or lower case
# var names cannot start with numbers
# commands like print must be exactly as defined

# Python Comments
# this is a comment, it is a line of code that will not be executed
# everything after the hashtag is ignored

'''
Using triple single quotes
is a way of doing a multiline comments
though technichally it's a 
multiline string that is not run by python
'''
"""
 this is a comment also
"""

# Shell vs python files
# the shell is a "sandbox" area where you can manipulate variables 
# the symbol >>> indicates that you can write and evalutate a line of python code
# python files are essentially text files with a .py file extension 
# this file is a python file

# Variables
# python variables are weakly typed, this means any variable can be any type of variable
# a is our variable here
a = 1
# variables can be updated
a = 2
# variables can be assiged to other vars
b = a

# variables have naming conventions
# variables should be descriptive, single letter vars should be avoided
this_is_a_snake_case_name_variable = 1
thisIsACamelCaseVar = 2
ALL_CAPS_VARS_ARE_COMMON_FOR_GLOBAL_VARS = 1354

# the print statements with a '#' are commented out, 
# you can uncomment them by deleting the # to see the output
#print(b)
#print(a) 
# variables can also be functions, but this is not necessary to understand right now
c = lambda x: x+1
#print(c(2))

# Basic Types and operators
# ints or integers are numbers without decimals
a = 1
b = 2
c = -11123123
# integers can be as big you want
a = 100000 ** 10000
#print(a)
d = 0

# floats are numbers with decimal points
a = 1.0
b = 1.0129384857
c = -1.234234

# booleans can be True or False, that's it!
a = True
b = False

# strings are sequences of characters
a = "useful strings"
b = "f"
#print(a)
# there are unicode strings 

# Basic Operators
# math
c = 1 + 1 # addition
b = 3 * 3 # multiplication
d = 5 / 3 # division
e = 3**4 # exponential 
# use brackets to enforce precedence
f = (3-3)*4
#print(f)

# Operations between different types of variables mean that one of the variables must be converted 
# ints are converted to floats
g = 4 + 3.5 # ie 4 (int) + 3.5 (float) becomes 4.0 + 3.5 which can be added and results in 7.5
#print(g)

# False and True are implicitely 0 and 1
h = False + 1 # converted to 0 + 1
i = True + 1
#print(i)

# strings can be added to create longer strings
a = "gotcha" + " " + "tongue"
#print(a)

# we can determine the types of variables
# we use the function 'type'
a = False
b = 1
#print(type(a))
#print(type(b))
true = False # try to avoid setting variables to be confusing like this!
#print(true)

# 'is' is a keyword to compare types of variables
a = False
#print(type(a) is bool) # this returns True, validating that the type of a is 'bool'
#print(a is bool) # this is incorrect, aka is comparing False is bool

# % is modulus aka remainder
a = 9 % 4 # what is the remainder of 9 / 4 ?
#print(a)

# Boolean Logic
# expressions that evaluate to True or False
a = True and False 
b = True or False
c = 1 <= 10
d = 3 >= 10
e = 4 > 10
f = 5 < 10
g = 4 == 2 + 2
h = (5 == 2+3) == False
#print(h)

# string comparisons are valid and useful to determine order 
a = "hi" < "abacus" # strings are compared based on alphabetic order
print(a)

# Strings
# get string length using 'len'
a = "a string"
length_of_a = len(a)
#print(length_of_a)
# get a single character of a string by indexing the string
first_char = a[0]
print(first_char)
first_3_letters = a[:3] # this is slicing syntax
print(first_3_letters)
first_3_letters = a[0:3] # we are slicing from index 0 inclusive to 3 exclusive

# Functions
# Tuples, Set, Lists, Dictionaries
# Loops


