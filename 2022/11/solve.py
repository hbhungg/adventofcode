with open('test.txt') as f:
  lst = f.readlines()
  lst = [i.strip() for i in lst]


class Monkey:
  def __init__(self, items, ops, div, tf):
    self.items = items
    self.ops = ops
    self.div = div
    self.tf = tf
  
  def opsexec(self, old):
    # Yea very dangerous
    # Also, very scuff
    ll = locals()
    exec(self.ops, None, ll) 
    return ll["new"]
  
  def act(self, v):
    if v % self.div == 0:
      return self.tf[0]
    else:
      return self.tf[1]

  def __repr__(self):
    return f"{self.items}"

class Number:
  prime = []
  def __init__(self, val=None):
    self.val = val
    self._factor = None

  @property
  def factor(self):
    if self._factor is None:
      ret = []
      for p in Number.prime:
        if self.val % p == 0:
          ret.append(p)
      if len(ret) == 0:
        ret.append(self.val)
      self._factor = ret
    return self._factor

  def __repr__(self):
    return f"{self.val}"

mks = dict()
lst = [lst[x:x+6] for x in range(0, len(lst), 7)]

for i in lst:
  monkey = int(i[0][-2])
  items = i[1].split(" ")[2:]
  items = list(map(lambda x: Number(val=int(x.strip(","))), items))
  ops = i[2].split(":")[1][1:]
  div = int(i[3].split(" ")[-1])
  t = int(i[4].split(" ")[-1])
  f = int(i[5].split(" ")[-1])
  mm = Monkey(items, ops, div, (t, f))
  mks[monkey] = mm

Number.prime = [i.div for i in mks.values()]
print(Number.prime)
print([i.items for i in mks.values()])
for v in mks.values():
  for i in v.items:
    print(i.val, i.factor)

#from collections import defaultdict
#mkret = defaultdict(lambda: 0)
#
## 20 round
#from tqdm import tqdm
#for i in tqdm(range(20)):
#  for k, v in mks.items():
#    mkret[k] += len(v.items)
#    for i in v.items:
#      new = v.opsexec(i)
#      actm = v.act(new)
#      mks[actm].items.append(new)
#    v.items = []
#
#p1 = sorted(mkret.values())
#print(mks)
#print(p1[-2] * p1[-1])
