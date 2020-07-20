# Time Complexity aka Computational Complexity 
# aka how hard is it or how long will it take in relative terms to operate on a certain dataset
# a complexity class is applicable to any function operating on a data set of size n
# cheat sheet: https://www.bigocheatsheet.com/

# Big Oh Notation
# this is how we describe how long it takes relatively to deal with a problem
# O(n) for example is the notation for linear time complexity

# complexity classes such as O(n) are a lower bounds
# this means that O(2n) is equivalent to O(n)

# O(1) or O(c) this is constant time aka instant
# an ex:
a = 1
a = a + 1 # this operation is O(1)
a = [1,2,3,4,5,6] 
print(len(a)) # getting the length of a list is O(1) 
a_dict = {e:e for e in range(1000000)} # this creates a large dictionary with 1 million elements in it
print(a_dict[10040]) # getting an element from a dictionary is O(1)

# O(logn) 
# this complexity class often applies to tree algorithms
# refer to Complexity cheat sheet

# O(n) means we do one operation for each element in a data set 
# aka n operations for n elements
# counting for example is O(n)
a = [1,5,7,8,8,6,4,3,2,5]
count = 0
for e in a:
    if e == 5:
        count += 1
        
# O(nlogn)
# this complexity class is common for sorting algorithms algorithms
a = [1,3,5,7,8,5,43]
sorted([a]) # this is nlogn 

# O(n**2)
# This complexity class is common for anything operating in 2 dimensions
# this includes matrices, doubly nested for loops, or any kind of loop
n = 10
for i in range(n):
    for j in range(n):
        print(i*j) # this operation will occur O(n**2) times
        
# O(n**3) 
# this complexity class applies to all operations in 3 dims
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i*j*k) # this operation will occur O(n**3) times
            
# O(2**n) Exponential for any base
# this could be described also as O(c**n)
# Exponential growth is a common problem type for this class
# if for example for each element you doubled the number of elements and operations you are working with then this would grow exponentially

# O(n!) Factorial Complexity 
# this is the largest we will deal with 
# the case example for this is calculating a factorial number
# we'll implement this later because it's an example of recursion


# EXAMPLES 
# what is the complexity class of the following

for i in range(n): # *n
    if i%2 == 0: # /2
        for j in range(n): # *n
            print(i*j) # 1
            
# We can assemble the complexity for the above as follows:            
# O(((1*n)/2)*n)
# O((n/2)*n)

# n         n**2
# -- x n = ------ = (1/2) x n**2
# 2           2 

# When assessing big O complexity we drop the constants 
# so in this case the complexity is simply O(n**2)

# We might be tempted to extrapolate from this that any nested list with 
# some other logic going on will reduce to the obvious complexity
# however thorough understanding of the operation of the logic is necessary 
# for example

for i in range(n): # *n
    if n==5: # /2
        for j in range(n): # *n
            print(i*j) # 1
            
# Understanding Complexity is useful in understanding when to make a trade off between computational and memory cost of an algorithm
# for example: 
# if we had a list of words ie strings and we want to sort each of these strings
list_of_strings = ["frog","hand","frog","left", "left"] # ,...this could have any large number of strings 
# sorting each string will take O(nlogn) time
# so if we know that there are many repetitions, it makes sense to cache the result of the sort
# we can validate that two strings are equal in O(n) time 
# O(n) for string comparison is less than O(nlogn) for string sorting
# this means we can improve our time by storing sorted strings in a dictionary aka hashmap

# our first approach is O(n*logn*n) = O(n**2 logn)
sorted_strings = []
for string in list_of_strings: # *n
    sorted_strings.append(sorted(string)) # this takes O(nlogn)
    
# if we only have a constant number C of different strings, then we can reduce our time complexity to that constant number
# If we cache our sorted results, the complexity reduces to O(n)
sorted_strings = []
seen_strings = {}
for string in list_of_strings: # *n
    if string not in seen_strings: # we will only sort the strings C times aka once for each unique string
        sorted_string = sorted(string) # this takes O(nlogn)
        sorted_strings.append(sorted_string) 
    else: # this will execute n-C times
        sorted_strings.append(seen_strings[string]) # 1    
    

