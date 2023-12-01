with open("input.txt") as f:
  lst = f.readlines()
  lst = [[int(p) for p in list(l.strip())] for l in lst]


STEP = 1000
flashes = 0

def pprint(lst):
  for dd in lst:
    print(dd)
  print()
  
def ripple(i, j):
  direct = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
  if 9 < lst[i][j]:
    lst[i][j] = 0
    global flashes
    flashes += 1
    for d in direct:
      it = i + d[0]
      jt = j + d[1]
      if -1 < it < len(lst) and -1 < jt < len(lst):
        if lst[it][jt] != 0:
          lst[it][jt] += 1 
          ripple(it, jt)
    
pprint(lst)
for s in range(STEP):
  for i in range(len(lst)):
    for j in range(len(lst)):
      if lst[i][j] < 10:
        lst[i][j] += 1
  #pprint(lst)

  # Flash and increase neighbour
  for i in range(len(lst)):
    for j in range(len(lst)):
      ripple(i, j)
  
  # After flash, set to 0
  #for i in range(len(lst)):
  #  for j in range(len(lst)):
  #    if lst[i][j] > 9:
  #      flashes += 1
  #      lst[i][j] = 0
  if sum([sum(l) for l in lst]) == 0:
    print(s)
  # pprint(lst)
print(flashes)
