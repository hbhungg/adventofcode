with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip() for l in lst]

def parse(l):
  turn, coord = l.split(" ")
  if turn == "on": turn = True
  else: turn = False

  coord = coord.split(",")
  coord = [[int(p) for p in l[2:].split("..")] for l in coord]
  return turn, coord

p1 = map(parse, lst)
on = {}

from tqdm import tqdm
for i in tqdm(p1):
  turn = i[0]
  coord = i[1]
  xs = coord[0]
  ys = coord[1]
  zs = coord[2]
  for x in range(xs[0], xs[1]+1):
    for y in range(ys[0], ys[1]+1):
      for z in range(zs[0], zs[1]+1):
        on[(x, y, z)] = turn

ret = 0
for x in range(-50, 50+1):
  for y in range(-50, 50+1):
    for z in range(-50, 50+1):
      if (x, y, z) in on:
        if on[(x, y, z)] is True:
          ret += 1

print(ret)
