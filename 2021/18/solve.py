with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip() for l in lst]

import ast
parse = [ast.literal_eval(l) for l in lst]

class Node:
  def __init__(self, left=None, right=None, value=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent

  def __str__(self):
    if self.value is not None:
      return str(self.value)
    else:
      return "[{}, {}]".format(self.left, self.right)

class StopExecution(Exception):
  pass
   
import math
class Tree:
  def __init__(self):
    self.root = Node()
  
  def construct(self, lst):
    Tree.__construct(lst, self.root)

  @staticmethod
  def __construct(lst, curr):
    if isinstance(lst, int):
      curr.value = lst
    else:
      temp = Node(parent=curr)
      curr.left = temp
      Tree.__construct(lst[0], temp)
      temp = Node(parent=curr)
      curr.right = temp
      Tree.__construct(lst[1], temp)


  def explode(self):
    try:
      Tree.__explode(0, self.root, None, None)
    except StopExecution:
      return True
    else:
      return False
  
  @staticmethod
  def __explode(depth, curr, right, left):
    # Check if the node is a pair or a regular number
    if curr.value is None:
      # Recursively go to each left and right node if they are not regular number
      if curr.left.value is None: Tree.__explode(depth+1, curr.left, curr.right, left)
      if curr.right.value is None: Tree.__explode(depth+1, curr.right, right, curr.left)

      # Print pair of regular numbers
      if curr.left.value is not None and curr.right.value is not None and depth >= 4:
        #print(curr, depth)
        if left is not None:
          # Find the rightmost regular number of the left side
          left_side = Tree.go_down(left, "r")
          # Add the left value of the exploding pair to it
          left_side.value += curr.left.value

        if right is not None:
          # Find the leftmost regular number of the right side
          right_side = Tree.go_down(right, "l")
          # Add the left value of the exploding pair to it
          right_side.value += curr.right.value
        # Replace the pair with 0
        curr.left = None
        curr.right = None
        curr.value = 0
        # Leftmost pair per execution
        #raise StopExecution

  @staticmethod
  def go_down(curr, side):
    if curr.value is None:
      if side == "r":
        return Tree.go_down(curr.right, side)
      if side == "l":
        return Tree.go_down(curr.left, side)
    else:
      return curr
    

  def split(self):
    try:
      Tree.__split(self.root) 
    except StopExecution:
      return True
    else:
      return False
    
  @staticmethod
  def __split(curr):
    if curr.value is not None:
      if curr.value >= 10:
        # Left and right value after split
        div = curr.value / 2
        leftval = math.floor(div)
        rightval = math.ceil(div)
        # Attach the value into the node
        curr.left = Node(value=leftval, parent=curr)
        curr.right = Node(value=rightval, parent=curr)
        # The node is now a pair
        curr.value = None
        # Leftmost regular number per execution
        raise StopExecution
    else:
      Tree.__split(curr.left)
      Tree.__split(curr.right)

  def add(self, tree):
    new_root = Node(self.root, tree.root)
    self.root = new_root

  def magnitude(self):
    return Tree.__magnitude(self.root)

  @staticmethod
  def __magnitude(curr):
    if curr.value is not None:
      return curr.value
    else:
      return Tree.__magnitude(curr.left) * 3 + Tree.__magnitude(curr.right) * 2

  def __str__(self):
    return str(self.root)

ret = []

# Shittiest attempt at 1am
for i in range(0, len(parse)-1):
  for j in range(i+1, len(parse)):
    v = Tree()
    v.construct(parse[i])
    temp = Tree()
    temp.construct(parse[j])
    v.add(temp)
    r = True
    z = True
    while (r or z) is True:
      r = v.explode()
      z = v.split()
    mag = v.magnitude()
    ret.append(mag)

    v = Tree()
    v.construct(parse[j])
    temp = Tree()
    temp.construct(parse[i])
    v.add(temp)
    r = True
    z = True
    while (r or z) is True:
      r = v.explode()
      z = v.split()
    mag = v.magnitude()
    ret.append(mag)

print(max(ret))
