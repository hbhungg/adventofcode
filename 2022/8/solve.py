import numpy as np

with open("input.txt") as f:
  lst = f.readlines()

lst = [list(map(int, list(i.strip()))) for i in lst]
trees = np.array(lst)
mmap = np.zeros((len(lst), len(lst)))

def look(ll, both=True):
  ret = np.zeros(len(ll))
  ret[0] = 1
  ret[-1] = 1

  # Too lazy
  mm = ll[0]
  for i in range(1, len(ll)):
    if ll[i] > mm:
      ret[i] = 1
      mm = ll[i]

  if both:
    mm = ll[-1]
    for i in reversed(range(1, len(ll))):
      if ll[i] > mm:
        ret[i] = 1
        mm = ll[i]
  return ret

#for i in range(len(lst)):
#  v1 = look(trees[i, :])
#  v2 = look(trees[:, i])
#  mmap[i, :] = np.logical_or(mmap[i, :], v1)
#  mmap[:, i] = np.logical_or(mmap[:, i], v2)
#
#print(mmap)
#print(mmap.sum())

def score(ll, h):
  ret = 0
  for i in ll:
    if i >= h:
      ret += 1
      break
    else:
      ret += 1
  return ret

m = 0
for i in range(len(lst)):
  for j in range(len(lst)):
    up = np.flip(trees[:i, j])
    down = trees[i+1:, j]
    right = trees[i, j+1:]
    left = np.flip(trees[i, :j])
    h = trees[i, j]
    ss = score(up, h)* score(down, h)* score(right, h)* score(left, h)
    #print(up, down, right, left,h, ss)
    #print(score(up, h), score(down, h), score(right, h), score(left, h))
    if m < ss:
      m = ss

print(trees)
print(m)
