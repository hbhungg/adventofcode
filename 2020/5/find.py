#!/usr/bin/env python3

with open('plane_seat.txt') as f:
  lines = f.read().split()


def r_rec(code, low, high, leng_h):
  if high == low:
    return low
  if code[len(code) - leng_h] in ['F', 'L'] :
    return r_rec(code, low, low  + (high-low)//2, leng_h-1)
  elif code[len(code) - leng_h] in ['B', 'R']:
    return r_rec(code, low + 1 + (high-low)//2, high, leng_h -1)

maxv = 0
seats = []
for i in lines:
  row = i[0:7]
  col = i[7:10]
  rval = r_rec(row, 0, 127, len(row))
  cval = r_rec(col, 0, 7, len(col))
  sid = rval * 8 + cval
  seats.append(sid)
  if maxv < sid:
    maxv = sid
print(maxv)
seats = sorted(seats)
for i in range(len(seats)-1):
  if seats[i+1] - seats[i] != 1:
    print(seats[i] + 1)
    break
