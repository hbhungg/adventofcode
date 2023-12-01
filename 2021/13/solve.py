with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip() for l in lst]

points = lst[:-13]
points = [[int(l) for l in sub.split(",")] for sub in points]
folds = lst[-12:]
folds = [l.split()[2] for l in folds]

for f in folds:
  line = int(f.split("=")[1])
  if f[0] == "x":
    for p in points:
      if p[0] > line:
        p[0] = line - abs(p[0]-line)   
  if f[0] == "y":
    for p in points:
      if p[1] > line:
        p[1] = line - abs(p[1]-line)   

def visulize(pts):
  dim_x = max(pts, key=lambda x: x[0])[0] + 1
  dim_y = max(pts, key=lambda y: y[1])[1] + 1
  ret = [["." for x in range(0, dim_x)] for y in range(0, dim_y)]
  for p in pts:
    x = p[1]
    y = p[0]
    ret[x][y] = "#"
  for r in ret:
    print(" ".join(map(str, r)))

reduc = set(tuple(row) for row in points)
visulize(reduc)
print(len(reduc))
