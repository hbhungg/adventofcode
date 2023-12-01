#!/usr/bin/env python3
import re
from functools import reduce
with open('passport.txt') as f:
  lines = f.read().split('\n\n')


def byr(value):
  return 1920 <= int(value) <= 2002

def iyr(value):
  return 2010 <= int(value) <= 2020

def eyr(value):
  return 2020 <= int(value) <= 2030

def hgt(value):
  if value[-2:] == 'cm':
    return 150 <= int(value[:-2]) <= 193
  if value[-2:] == 'in':
    return 59 <= int(value[:-2]) <= 76
  else:
    return False

def hcl(value):
  if re.fullmatch('^#([0-9]|[a-f]){6}$', value) is not None:
    return True
  return False

def ecl(value):
  return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(value):
  return len(value) == 9

def cid(value):
  return True

fields = {'byr': byr, 'iyr': iyr, 'eyr': eyr, 'hgt': hgt, 'hcl': hcl, 'ecl': ecl, 'pid': pid, 'cid': cid}

count = 0
for passport in lines:
  passport = passport.split()
  temp = []
  r = True
  if len(passport) < 7:
    r = not r 
  elif len(passport) == 7:
    for p in passport:
      if p[0:3] == 'cid':
        r = not r
  t = 0
  if r is True: 
    for p in passport:
      tag = p[0:3]
      value = p[4:]
      temp.append(fields[tag](value))
    t = reduce((lambda x, y: x * y), temp)
  count += t
  if t == 1:
    print(passport)
print(count)
