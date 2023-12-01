#!/usr/bin/env python3

with open('rules.txt') as f:
  lines = f.read().split('\n')

def find_base(color):
  contain = [color]  

  for c in contain:
    for i in lines:
      color_c = ' '.join(i.split()[0:2])
      color_cd = ' '.join(i.split()[3:])
      if c in color_cd:
        contain.append(color_c)
  contain = set(contain[1:])
  return contain, len(contain)

print(find_base('shiny gold'))

