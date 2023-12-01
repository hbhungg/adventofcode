with open("test.txt") as f:
  lst = f.readlines()
  lst = [i.strip() for i in lst]

from collections import defaultdict

def traverse(lst, head=0, d=defaultdict(int), curr_d=None):
  if head >= len(lst):
    return 0
  ll = lst[head]
  pp = ll.split(" ")
  print(ll)
  match pp:
    case [_, "cd", _]:
      traverse(lst, head+1, d, curr_d=pp[2])
    case [_, "ls"]:
      sz = traverse(lst, head+1, d, curr_d)
      d[curr_d] = sz
    case ["dir", _,]:
      traverse(lst, head+1, d, curr_d)
      pass
    case _:
      # print(ll)
      fsz = traverse(lst, head+1, d, curr_d)
      print("DEBUG", ll, fsz)
      return 0 + int(pp[0])

traverse(lst)
