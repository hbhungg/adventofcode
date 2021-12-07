with open("input.txt") as f:
  lst = f.readlines()[0].strip().split(",")
  lst = [int(l) for l in lst]

MAX = max(lst)
MIN = min(lst)

print(MAX, MIN) 

ret = []
for i in range(MIN, MAX+1):
  ret.append(sum([sum(range(1, abs(i-l)+1)) for l in lst])) 

print(min(ret))
