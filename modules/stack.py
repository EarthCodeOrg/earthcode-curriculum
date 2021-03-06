# Stack 
# FILO - First In Last Out
# is a data structure that you add elements only at the "top" and remove elements also only at the "top"
# we will use a list as if it were a stack
a_stack = []
a_stack.append(1) # for a stack we can only append, we cannot insert at any specific or indexed location
print(a_stack)
# we examine the top of  the stack by "peeking"
# this simply means looking at the top element without removing it
a_stack[-1] # we would peek using indexing the last element
last_element = a_stack.pop() # we can only pop and remove elements from the end of the stack
print(last_element)

# we usually would implement a stack as a linked list to get O(1) insertion and deletion


# Queue
# FIFO - First In First Out 
# a queue is used such that elements are added to the "back" of the queue and removed from the "front"
a_queue = []
# INSERTING is done at the back
a_queue.append(1)
# REMOVAL is done at the front
a_queue.pop(0)

# queues are often implemented also with a linked list which enables O(1) performance for insertion and deletion

