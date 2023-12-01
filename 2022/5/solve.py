with open("input.txt") as f:
  lst = f.readlines()
  lst = [i.strip() for i in lst]

start = []
ins = []
g = False
for i in lst:
  if i == "": g = True
  elif g: ins.append(i)
  else: start.append(i)

stack = {}

for i in start:
  for j in range(0, len(i), 4):
    crate = i[j:j+4].strip(" []")
    if crate.isdigit():
      break
    if crate != "":
      pos = j//4+1
      if pos not in stack:
        stack[pos] = [crate]
      else:
        stack[pos].append(crate)

# Reverse them all
for k, v in stack.items():
  stack[k] = v[::-1]

for i in ins:
  v = i.split(" ")
  amount, curr, des = int(v[1]), int(v[3]), int(v[5])
  temp = []
  for t in range(amount):
    temp.append(stack[curr].pop()) 
  
  # Comment and uncomment these 2 for results of different part
  stack[des].extend(temp) # Part 1
  #stack[des].extend(reversed(temp)) # Part 2


ret = ""
for i in range(1, 10):
  ret += stack[i][-1]

print(ret)



