# RECURSION
# recursion is simply a function calling itself, or a small collection of functions that are calling themselves
def a_recursive_func(a):
    if a < 1:
        print(a)
        a += 1
        a_recursive_func(a)

#a_recursive_func(-10)

# loops are built with recursion under the hood (in assembly for ex)
# pretty much everything is recursive at some low level

# here's an example of a recursive loop function and its corresponding standard loop
def loop_through_range(index, start, inc, end, func):
    if index < end:
        func(index)
        loop_through_range(index+inc, start, inc, end, func) 

def func(i): 
    print(i)

#loop_through_range(0,0, 1, 10, func)

for i in range(10):
    #print(i)
    pass
    
# the two iterative approaches above do essentially the same thing
# except the recursive version has a larger "overhead" 
# that is why we get max recursion depth errors if we try to recurse infinitely

# recursive functions have base cases and recursive cases
# base cases are end cases ie when you want the recursion to be done

def adds_a_word_to_a_list_until_list_has_five_words(a_list, a_word):
    if len(a_list) == 5: # this is our base case, we are done recursion when we get here
        return a_list # this list that we return is returned back up to the layer above it
    if len(a_list) != 5: # this is our recursive statement
        a_list.append(a_word)
        return adds_a_word_to_a_list_until_list_has_five_words(a_list, a_word)
        
a_list = adds_a_word_to_a_list_until_list_has_five_words([],"pickle")
print(a_list)
    
# calculating the ith fibonacci element can solved
# 1,1,2,3,5,8,11, ...
# 0 1 2 3 4 5 6

# f(0) = 1
# f(1) = 1
# f(2) = f(1)+f(0) = 2
# f(3) = f(2)+f(1) = 3
# f(i) = f(i-1) + f(i-2)

def fibonacci(i):
    if i == 0:
        return 1
    if i == 1: 
        return 1
    if i > 1:
        return fibonacci(i-1) + fibonacci(i-2)
        
print(fibonacci(5))
#print(fibonacci(1000)) # this takes a reaaaally long time if ever!

# recursing on fibonacci creates a recursion tree as follows
# 4           5
# 3         3          
# 2      2       2
# 1       1  1    1
# 0     1       1 

# this implies that the recursion tree for fibonacci has a complexity of 
# 2**n since for every invocation of the function , two more function calls are made
# practically this is a terrible function and implemention even though it's a good example

# another example: getting the sum of the numbers of a list 
def recursive_sum(a_list):
    if len(a_list) == 0: # A
        return 0
    if len(a_list) == 1: # B 
        return a_list[0]
    return a_list.pop() + recursive_sum(a_list) # C

sum_a = recursive_sum([1,3,5,7,8,9])
print(sum_a)

# we're going to trace how this function executes
# [1,3,5,7,8,9] -> A:FALSE, B:FALSE, C: 9+recursive_sum([1,3,5,7,8])
# [1,3,5,7,8] -> A:FALSE, B:FALSE, C: 8+recursive_sum([1,3,5,7])
# [1,3,5,7] -> A:FALSE, B:FALSE, C: 7+recursive_sum([1,3,5])
# [1,3,5] -> A:FALSE, B:FALSE, C: 5+recursive_sum([1,3])
# [1,3] -> A:FALSE, B:FALSE, C: 1+recursive_sum([1])
# [1] -> 1





