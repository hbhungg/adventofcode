with open("input.txt") as f:
  lst = f.readlines()
  lst = [list(l.strip()) for l in lst]
  lst = [[int(p) for p in l] for l in lst]

def neighbour(node, size):
  x, y = node
  direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  retval = []
  for d in direction:
    x_t = x + d[0] 
    y_t = y + d[1] 
    if -1 < x_t < size and -1 < y_t < size:
      retval.append((x_t, y_t))
  return retval

start = (0, 0)
# Distance from (0, 0) to every other node
dist = {(v, u):float("inf") for v in range(len(lst)*5) for u in range(len(lst)*5)}
# Starting node is 0 distance
dist[start] = 0 
visited = {(u, v): False for v in range(len(lst)*5) for u in range(len(lst)*5)}

from queue import PriorityQueue
pq = PriorityQueue()
pq.put((0, (0, 0)))

size = 5
dest = (len(lst)*size-1, len(lst)*size-1)

while not pq.empty():
  _, curr = pq.get()
  visited[curr] = True
  for n in neighbour(curr, len(lst)*size):
    # Original coord
    ox, oy = n[0] % len(lst), n[1] % len(lst)
    # Original val
    ds = lst[ox][oy]
    # New val
    fx, fy = n[0] // len(lst), n[1] // len(lst)
    for i in range(fx + fy):
      ds += 1
      if ds > 9:
        ds = 1
    if visited[n] == False:
      old = dist[n]
      new = dist[curr] + ds
      if new < old:
        pq.put((new, n))
        dist[n] = new

print()
print(dest)
print(dist[dest])
