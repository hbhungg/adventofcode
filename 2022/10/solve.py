with open('input.txt') as f:
  lst = f.readlines()
  lst = [i.strip() for i in lst]

x_reg = 1
clock = 1
addr = 0
xs = {1: 1}

while addr < len(lst):
  op = lst[addr].split(" ")
  if op[0] == "noop":
    clock += 1
    xs[clock] = x_reg
  elif op[0] == "addx":
    clock += 1
    xs[clock] = x_reg
    clock += 1
    x_reg += int(op[1])
    xs[clock] = x_reg
  addr += 1

ret = 0
for i in range(20, 221, 40):
  ret += i*xs[i]
print(ret)

crt = []
row = ""

for r in range(6):
  for c in range(1, 41):
    spr = xs[r * 40 + c]
    if spr - 1 <= c-1 <= spr + 1:
      row += "#"
    else:
      row += "."
  crt.append(row)
  row = ""

for i in crt:
  print(i)
