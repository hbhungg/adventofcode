#!/usr/bin/env python3

f = open('input.txt', 'r')

def valid_check(low, high, letter, value):
  return (value[low-1] == letter and not value[high-1] == letter) or (not value[low-1] == letter and value[high-1] == letter)  
 
  
counter = 0
passwords = []
for i in f:
  password = i.split()
  passwords.append(password)
  low = int(password[0].split('-')[0])
  high = int(password[0].split('-')[1])
  letter = str(password[1][0])
  value = str(password[2])
  if valid_check(low, high, letter, value):
    counter += 1

print(counter)
print(len(passwords))
