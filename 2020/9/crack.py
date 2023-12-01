#!/usr/bin/env python3

with open('encrypted.txt') as f:
  lines = f.read().split()

def enum_sum(l, n):
  for i in l:
    for j in [x for x in l if x != i]:
      if int(i) +int(j) == int(n):
        return True
  return False

#for l in range(26, len(lines)):
#  p = lines[l-26:l] 
#  value = lines[l]
#  if enum_sum(p, value) is False:
#    print(value)
#    break

inv_num = 466456641
lines = list(map(int, lines))
size = 2
for i in range(len(lines)):
  for j in range(len(lines)):
    con_temp = lines[j:j+size+1]
    if sum(con_temp) == inv_num:
      print(min(con_temp), max(con_temp))
      print(min(con_temp) + max(con_temp))
      break
  size += 1
