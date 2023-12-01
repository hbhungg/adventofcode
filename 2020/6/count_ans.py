#!/usr/bin/env python3
import re

with open('answer.txt') as f:
  lines = f.read().split('\n\n')

ans = []
for l in lines:
  l = l.split()
  ans.append(l)

count = 0
for a in ans:
  if len(a) == 1:
    count += len(a[0])
  else:
    res = a[0]
    for i in a:
      res = set(res).intersection(i)
    count += len(res)
print(count)
