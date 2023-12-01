with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip() for l in lst]

template = list(lst[0])
rules = lst[2:]
rules_d = {}

for r in rules:
  a, b = r.split(" -> ")
  rules_d[a] = b


ret = {}
for i in range(2, len(template) + 1):
  pair = "".join(template[i-2:i])
  if pair in ret:
    ret[pair] += 1
  else:
    ret[pair] = 1

ele = {}
for i in template:
  if i in ele:
    ele[i] += 1
  else:
    ele[i] = 1

for s in range(40):
  temp = {}
  for pair in ret:
    mid = rules_d[pair]
    amount = ret[pair]
    pair1 = pair[0] + mid
    pair2 = mid + pair[1]
    if mid in ele:
      ele[mid] += amount
    else:
      ele[mid] = 1

    if pair1 in temp:
      temp[pair1] += amount
    else:
      temp[pair1] = amount
    if pair2 in temp:
      temp[pair2] += amount
    else:
      temp[pair2] = amount
  ret = temp


print(ret)
print(ele)
print(sum(ret.values())+1)
print(sum(ele.values()))
print()
print(max(ele.values()))
print(min(ele.values()))
print(max(ele.values()) - min(ele.values()))
