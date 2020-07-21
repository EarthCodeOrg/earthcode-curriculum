# Trees
'''
      (4)
    /    \
  (5)    (7)
           \
            (9)
'''
# Trees are composed of 
# Nodes
#   The "Top" or "first" node is the root node  (4)
#   Each of the nodes that have no Children are called leaf nodes (5,7)
#   Parent nodes are nodes that are above a given node
#   Child nodes are nodes that are below a given node
#   Branches are another name for child nodes
# Edges that connect the nodes 
# Each node has 0 or more children

# Binary Trees simply has exactly 0 or 2 Branches/children per node
'''
      (4)
    /    \
  (5)    (7)
        /   \
      (2)   (9)
'''

# Binary Search Tree
# is a binary tree with 0,1,2 children per node where 
# all the elements of the left subtree are less than the value of the node and 
# all the elements of the right subtree are greater than the node
'''
      (10)
    /    \
  (5)    (17)
        /   \
      (12)   (19)

The number of elements per row grows exponentially so this allows our search depth ie search time to be log2(n)
1 
2
4
8
16
'''

class TreeNode():
  def __init__(self, value, left, right):
    self.value = value 
    self.left = left 
    self.right = right

class BinarySearchTree():
  def __init__(self):
    self._root = None

  def add(self, value, curr=None):
    if (self._root == None):
      self._root = TreeNode(value, None, None)
      return 
    if (curr==None): 
      self.add(value, self._root)
    elif (value < curr.value and curr.left != None):
      self.add( value, curr.left)
    elif (value > curr.value and curr.right != None):
      self.add( value, curr.right)
    elif (value < curr.value and curr.left == None):
      curr.left = TreeNode(value, None, None)
    elif (value > curr.value and curr.right == None):
      curr.right = TreeNode(value, None, None)

  def display_values_pre_order(self, curr=None):
    # Pre order 
    # Node, Left, Right
    if curr==None and self._root:
      self.display_values_pre_order(self._root)
    else:
      # Visit the node, simply print the value
      print(curr.value)
      # Recurse on left side
      if (curr.left):
        self.display_values_pre_order(curr.left)
      # Recurse on right side
      if (curr.right):
        self.display_values_pre_order(curr.right)

  def display_values_in_order(self, curr=None):
    # In order
    # Node, Left, Right
    if curr==None and self._root:
      self.display_values_in_order(self._root)
    else:
      if (curr.left):
        self.display_values_in_order(curr.left)
      print(curr.value)
      if (curr.right):
        self.display_values_in_order(curr.right)

def display_values_post_order(self, curr=None):
    # Post order
    # Node, Left, Right
    if curr==None and self._root:
      self.display_values_post_order(self._root)
    else:
      if (curr.left):
        self.display_values_post_order(curr.left)
      if (curr.right):
        self.display_values_post_order(curr.right)
      print(curr.value)

# Balanced Tree

if __name__ == "__main__":
  bst = BinarySearchTree()
  bst.add(3)
  bst.add(2)
  bst.add(10)
  bst.add(11)
  bst.add(9)
  '''
         (3)
        /  \
      (2)   (10)
           /   \
          (9)   (11)

  '''

  print("pre order")
  bst.display_values_pre_order()
  print("in order")
  bst.display_values_in_order()
