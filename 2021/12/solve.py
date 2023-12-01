with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip().split("-") for l in lst]


def traverse(g, node, des, visited, path):
  path.append(node)
  if not node.isupper():
    visited[node] += 1
  if visited[node] == 2:
    path[0] = node
  if node == des:
    print("ans", path)
  else:
    for i in g[node]:
      if i != "start":
        if path[0] is False:
          if visited[i] < 2:
            traverse(g, i, des, visited, path)
        if path[0] is not False:
          if visited[i] < 1:
            traverse(g, i, des, visited, path)
  some = path.pop()
  if some == path[0]:
    path[0] = False
  visited[node] -= 1

def top(lst):
  flat_lst = [i for sub in lst for i in sub]
  nodes = set(flat_lst)
  graph = {}
  visited = {}
  for n in nodes:
    graph[n] = []
    visited[n] = 0

  for p in lst:
    graph[p[0]].append(p[1]) 
    graph[p[1]].append(p[0])
  #print(graph) 
  path = [False]
  traverse(graph, "start", "end", visited, path)

top(lst)
