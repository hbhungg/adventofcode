with open("input.txt") as f:
  lst = f.readlines()
  lst = [i.strip().split() for i in lst]

def idd(a):
  # Rock, paper, scissor
  dd = [("XA", 0), ("BY", 1), ("CZ", 2)]
  for i in dd:
    if a in i[0]: return i[1]

def idd_ret(a):
  dd = {"X": False, "Y": None, "Z": True}
  return dd[a]

def compare(p1, p2):
  # True if a beat b, False otherwise
  # None if draw
  if p1 == p2: return None
  return ((p1 - p2) % 3) < 3/2

def choose(opp, outcome):
  if outcome is None:
    return opp
  ll = [0, 1, 2]
  ll.remove(opp)
  for i in ll:
    if i != opp:
      if (((i-opp) % 3) < 3/2) == outcome:
        return i


## Part 1
#score = 0
#for i in lst:
#  p1, p2 = idd(i[0]), idd(i[1])
#  score += p2 + 1
#  outcome = compare(p1, p2)
#  if outcome is False: score += 6
#  elif outcome is None: score += 3


# Part 2
score = 0
for i in lst:
  p1, outcome = idd(i[0]), idd_ret(i[1])
  p2 = choose(p1, outcome)
  score += p2 + 1
  if outcome is True: score += 6
  elif outcome is None: score += 3

print(score)
