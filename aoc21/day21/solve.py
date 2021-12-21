class Player:
  def __init__(self, pos, score=0):
    self.pos = pos
    self.score = score

  def check(self):
    if self.score >= 1000:
      return True
    return False

  def move(self, step):
    self.pos += step
    # Range 1 - 10 wrap around
    self.pos = 1 + (self.pos - 1) % (11 - 1)
    self.score += self.pos

class DDie:
  def __init__(self):
    self.curr = 0
    self.times = 0

  def roll(self):
    ret = []
    for i in range(3):
      self.times += 1
      self.curr += 1
      # Range 1 - 100 wrap around
      self.curr = 1 + (self.curr - 1) % (101 - 1)
      ret.append(self.curr)
    return ret

import itertools
from functools import cache
throws = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]

@cache
def play(turn, p1, p2, s1, s2, roll):
  global ret
  # Player 1 turn
  if turn is True:
    p1 += roll 
    # Wrap position
    p1 = 1 + (p1 - 1) % (11 - 1)
    s1 += p1
  if turn is False:
  # Player 2 turn
    p2 += roll
    p2 = 1 + (p2 - 1) % (11 - 1)
    s2 += p2

  # Check for winner
  if s1 >= 21:
    return 1, 0
  if s2 >= 21:
    return 0, 1
  sub = [play(not turn, p1, p2, s1, s2, t) for t in throws]
  return sum(a for a, b in sub), sum(b for a, b in sub)


ret = [play(True, 6, 8, 0, 0, t) for t in throws]
#print(ret)
print(sum(a for a, b in ret), sum(b for a, b in ret))
