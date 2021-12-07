
class Node:
  def __init__(self, value, neighbour_right):
    self.value = value
    self.neighbour_right = neighbour_right

class CircleList:
  """
  A static length Circle list
  Transform a list into a Circle list
  Support wrap around when iterating
  """
  def __init__(self, lst):
    self.length = len(lst)
    self.idxs = {}
    # The first Node to be create
    self.base_node = Node(lst[-1], None)
    # The current iterator Node in the Circle
    # After the construction, the self.current will hold the first value of the list
    self.current = self.base_node
    self.idxs[lst[-1]] = self.current
    # Construct the Circle
    for i in range(self.length-2, -1, -1):
      new_node = Node(lst[i], self.current)
      self.current = new_node
      self.idxs[lst[i]] = self.current
    self.base_node.neighbour_right = self.current

  def __len__(self):
    return self.length

  def __iter__(self):
    return self

  def __next__(self):
    current = self.current
    self.current = self.current.neighbour_right
    return current

  def __str__(self):
    retval = "["
    curr = self.base_node
    for i in range(self.length):
      retval = retval + "," + str(curr.value)
      curr = curr.neighbour_right
    retval += "]"
    return retval
  
  def index(self, value):
    return self.idxs[value]

  def insert(self, node, insert_node):
    right = node.neighbour_right
    node.neighbour_right = insert_node 
    insert_node.neighbour_right = right

  def pop(self, node):
    retval = node.neighbour_right
    right = node.neighbour_right.neighbour_right 
    node.neighbour_right = right
    return retval

if __name__ == "__main__":
  cup = list('716892543')
  cup = list('389125467')
  cup = [int(d) for d in cup]
  MOVE = 10000000
  MAX = max(cup)
  for i in range(MAX+1, 10**6+1):
    cup.append(i)  
  cl = CircleList(cup)
  for i in range(MOVE):
    pick = []
    curr = cl.current
    curr_val = curr.value
    for j in range(3):
      node = cl.pop(curr)
      pick.append(node)
    #print(cl)
    #print([l.value for l in pick])
    target = curr_val
    while True:
      target -= 1
      if target == 0:
        target = MAX
      if target not in [l.value for l in pick]:
        break 
    dest = cl.index(target)
    for i in range(2, -1, -1):
      cl.insert(dest, pick[i])
    next(cl)
    #print(cl)
  dest = cl.index(1)
  print(dest.neighbour_right.value)
  print(dest.neighbour_right.neighbour_right.value)
  print(dest.neighbour_right.value * dest.neighbour_right.neighbour_right.value)
