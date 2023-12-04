with open("input.txt") as f:
  d = [i.strip() for i in f.readlines()]

from icecream import ic
import re
import uuid

nn = {}
cd = {}
for idx, l in enumerate(d):
  # print(l)
  ms = re.finditer(r'\d+', l)
  for m in ms:
    s=m.start()
    e=m.end()
    t=m.group()
    # ic(s, e, t)
    idd = uuid.uuid4()
    nn[(idx, s)] = (t, idd)
    nn[(idx, e-1)] = (t, idd)

  cms = re.finditer(r'[^.\d]', l)
  for m in cms:
    s=m.start()
    e=m.end()
    t=m.group()
    # ic(s, e, t)
    cd[(idx, s)] = t


s1 = 0
s2 = 0
for k, v in cd.items():
  seen = []
  gear = 1
  # print(v)
  for x in range(-1, 2):
    for y in range(-1, 2):
      tx = k[0] + x
      ty = k[1] + y
      luval = nn.get((tx, ty), None)
      if luval:
        num, iid = luval
        if luval not in seen:
          seen.append(luval)
          s1 += int(num)
          if v == "*":
            # print(v, num)
            gear *= int(num)
  if len(seen) == 2:
    s2 += gear
  #         print(tx, ty, num)
  # print()

print(s1)
print(s2)
