with open("input.txt") as f:
  lines = f.readlines()
  lines = [[sub.split(",") for sub in l.strip().split(" -> ")] for l in lines]


def solve(ls):
  ret = {}
  for l in ls:
    curr = l[0]
    dest = l[1]
    if curr[0] <= dest[0]:
      xs = range(curr[0], dest[0]+1)
    else:
      xs = range(curr[0], dest[0]-1, -1)

    if curr[1] <= dest[1]:
      ys = range(curr[1], dest[1]+1)
    else:
      ys = range(curr[1], dest[1]-1, -1)
    path = (xs, ys)
    print(curr, dest, path)
    if len(path[0]) == 1 or len(path[1]) == 1:
      for i in path[0]:
        for j in path[1]:
          if ret.get((i, j)) is not None:
            ret[(i, j)] += 1
          else:
            ret[(i, j)] = 1
    else:
      for i, j in zip(path[0], path[1]):
          if ret.get((i, j)) is not None:
            ret[(i, j)] += 1
          else:
            ret[(i, j)] = 1
  print(ret)
  count = 0
  for val in ret.values():
    if val > 1:
      count += 1
  return count

prob1ls = [[[int(p) for p in ps] for ps in l] for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]
prob2ls = [[[int(p) for p in ps] for ps in l] for l in lines]

print(solve(prob1ls))
print(solve(prob2ls))

