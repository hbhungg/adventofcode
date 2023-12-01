with open("input_t.txt") as f:
  lst = f.readlines()

lst = [i.strip() for i in lst]

class Knot:
  def __init__(self):
    self.start = 0,0
    self.head = 0,0
    self.tail = 0,0
    self.di = {"D": (-1, 0), "U": (1, 0), "R": (0, 1), "L": (0, -1)}

  def move(self, d, s):
    mm = self.di[d]
    self.head = (self.head[0] + mm[0] * s, self.head[1] + mm[1] * s)

  def snap(self):


kk = Knot()
for i in lst:
  print(i, kk.head)
  d, s = i.split(" ")
  s = int(s)
  kk.move(d, s)
