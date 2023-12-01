with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip() for l in lst]

def check(m, i, j):
  direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for d in direction:
    i_t, j_t = i + d[0], j + d[1]
    if i_t > -1 and i_t < len(m) and j_t > -1 and j_t < len(m[0]):
      if int(m[i_t][j_t]) <= int(m[i][j]):
        return False
  return True
       

dim_x = len(lst)
dim_y = len(lst[0])
low = []
ret = 0
for i in range(0, dim_x):
  for j in range(0, dim_y):
    if check(lst, i, j) is True:
      ret += int(lst[i][j]) + 1 
      low.append((i, j))

print(ret)

def rev(bmap, m, i, j):
  direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for d in direction:
    i_t, j_t = i + d[0], j + d[1]
    if i_t > -1 and i_t < len(m) and j_t > -1 and j_t < len(m[0]):
      if bmap[i_t][j_t] is False:
        bmap[i_t][j_t] = True
        rev(bmap, m, i_t, j_t)

ret = []
for lw in low:
  bmap = [[False if int(p) < 9 else None for p in l] for l in lst]
  rev(bmap, lst, lw[0], lw[1])
  ret.append(sum([l.count(True) for l in bmap]))

ret = sorted(ret, reverse=True)
import math
print(math.prod(ret[:3]))
