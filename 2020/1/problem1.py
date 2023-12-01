#!/usr/bin/env python3
f = open('input.txt', 'r')
values = []
for i in f:
  values.append(int(i))

for index, a_value in enumerate(values):
  for b_value in values[:index]:
    for c_value in values[:index+1]:
      if a_value + b_value + c_value == 2020:
        print(a_value, b_value, c_value)
        print(a_value * b_value * c_value)
