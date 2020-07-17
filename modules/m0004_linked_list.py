# Linked Lists!
# A linked list is a type of list that is formed of a bunch of nodes that are connected to each other 
# linked lists have an insertion time of O(1) which makes them useful in some cases where an array is too slow
# the arrows below represent the connections from one node to another
# head -> (1) -> (5) -> (-2) -> tail
# adding a new element means we just have to "look" at where the tail is and insert the new element there
# head -> (1) -> (5) -> (-2) -> (1000) <- tail

class Node():
    def __init__(self, val, next): 
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None # this variable will point to a Node
        self.tail = None # this variable will also point to a Node
        
    def append(self, val):
        if self.head == None and self.tail == None:
            node = Node(val, None)
            self.head = node
            self.tail = node
        else:
            node = Node(val, None)
            self.tail.next = node
            self.tail = node
            
    def get(self, index):
        curr = self.head
        for i in range(index): # we traverse the list by moving a pointer variable ie curr to point at successive nodes
            if (curr.next == None): 
                raise IndexError("Index out of Bounds: " + str(index))
            curr = curr.next
        return curr.val
    
    def size(self):
        # implement a function that returns the length of the linkedlist
        pass
    
    def indexOf(self, value):
        # return the index of the first occurance of value
        # else -1 if it does not exist in the list
        pass
    
    def delete(self, index): 
        # method to delete element at index
        # raise error if index is out of bounds
        pass
  
ll = LinkedList()
ll.append(10)
ll.append(4)
ll.append(6)
# head -> (10) -> (4) -> (6) -> None   
# curr ----|  at the beginning of our get function , curr points to the head
#          |
# head -> (10) -> (4) -> (6) -> None 

# walking through ll.get(5)
# curr = (10)
# i = 0, curr = (4)
            
            
        
        