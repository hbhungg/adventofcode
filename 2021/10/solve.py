with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip() for l in lst]
  
pairs = {"(": ")", "{":"}", "[":"]", "<":">"}
points = {")": 3, "]":57, "}": 1197, ">": 25137}
op = "([{<"
cl = ")]}>"

def complete(ls):
  ret = ""
  pairs = {"(": ")", "{":"}", "[":"]", "<":">"}
  points = {")": 1, "]":2, "}": 3, ">": 4}
  for l in ls:
    ret = ret + pairs[l]
  ret = reversed(ret)
  p = 0
  for r in ret:
    p = 5 * p + points[r] 
  return p

ret = 0
inc = []
zz = []
for l in lst:
  stack = []
  incheck = False
  for c in l:
    if c in op:
      stack.append(c)
    if c in cl:
      if pairs[stack[-1]] == c:
        stack.pop()
      else:
        ret += points[c]
        incheck = True
        break
  if incheck is not True:
    zz.append(l)
    inc.append(complete(stack))

print(ret)
print(sorted(inc)[(len(inc)-1)//2])
