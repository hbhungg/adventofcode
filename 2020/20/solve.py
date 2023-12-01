with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip() for l in lst]
  lst = [l for l in lst if l != '']

tiles = {}
for i in range(0, len(lst), 11):
  idx = lst[i][5:-1] 
  pic = lst[i+1: i+11]
  tiles[idx] = pic

