with open("input.txt") as f:
  lst = f.readlines()
  lst = [i.strip() for i in lst]

def prio(a):
  if a.isupper():
    return ord(a) - 38
  else:
    return ord(a) - 96

score = 0
for i in lst:
  mid = len(i)//2
  h1, h2 = i[:mid], i[mid:]
  ss1, ss2 = set(h1), set(h2)
  same = list(ss1 & ss2)
  score += prio(same[0])

print(score)


score = 0
for i in range(0, len(lst), 3):
  f1, f2, f3 = set(lst[i]), set(lst[i+1]), set(lst[i+2]) 
  same = list(f1 & f2 & f3)
  score += prio(same[0])

print(score)
