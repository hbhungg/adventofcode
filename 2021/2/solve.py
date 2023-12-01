#!/usr/bin/python3

with open("input.txt") as f:
  lines = f.readlines()
  lines = [l.strip() for l in lines]
horiz = 0
depth = 0
aim = 0
for move in lines:
  parse = move.split()
  parse[1] = int(parse[1])
  if parse[0] == "forward":
    horiz += parse[1]
    depth += aim*parse[1]
  if parse[0] == "down":
    aim += parse[1]
  elif parse[0] == "up":
    aim -= parse[1]
    

print(horiz, depth)
print(horiz*depth)
