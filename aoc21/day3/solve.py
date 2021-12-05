from collections import Counter

with open("input.txt") as f:
  lines = f.readlines()
  lines = [l.strip() for l in lines]

retval = []
retval1 = []
for i in range(len(lines[0])):
  temp = sum([int(l[i]) for l in lines])
  if temp > len(lines)-temp:
    retval.append(1)
    retval1.append(0)
  else:
    retval.append(0)
    retval1.append(1)


def tobit(bitlist):
  out = 0
  for bit in bitlist:
    out = (out << 1) | bit
  return out

#val1 = tobit(retval)
#val2 = tobit(retval1)
#print(val1*val2)

def prob2(ls, pos):
  ones = []
  zeros = []
  for l in ls:
    if l[pos] == "1":
      ones.append(l)
    elif l[pos] == "0":
      zeros.append(l)
  if len(zeros) > len(ones):
    return zeros, ones
  return ones, zeros

ret = lines
vv = lines
for i in range(len(lines[0])):
  if len(ret) > 0:
    ret,_ = prob2(ret, i)
  if len(vv) > 1:
    _, vv = prob2(vv, i)
print(int(ret[0], 2))
print(int(vv[0], 2))

