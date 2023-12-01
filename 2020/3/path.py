#!/usr/bin/env python3

with open('map.txt') as f:
  mapp = f.read().splitlines()

def traverse(r, d):
  tree = 0
  length = 31
  v = 0
  for i in range(0, len(mapp), d):
    if mapp[i][v % length] == '#':
      tree += 1
    v += r 
  return tree

print(traverse(3, 1)) 
print(traverse(1, 1))
print(traverse(5, 1))
print(traverse(7, 1))
print(traverse(1, 2))
