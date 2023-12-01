x = range(211, 232+1)
y = range(-69, -124 - 1, -1)

print(list(x))
print(list(y))



def calc(x, y, velocity):
  start = [0, 0]
  curr = start 
  max_y = 0
  while True:
    # x velocity 
    curr[0] += velocity[0] 
    # y velocity
    curr[1] += velocity[1]

    # Drag
    if velocity[0] > 0:
      velocity[0] -= 1
    elif velocity[0] < 0:
      velocity[0] += 1

    velocity[1] -= 1
    if curr[1] > max_y:
      max_y = curr[1]
    if x[0] <= curr[0] <= x[-1] and y[0] >= curr[1] >= y[-1]:
      return True, max_y
    if curr[1] < y[-1]:
      return False, None

ret = []
total = 0
from tqdm import tqdm
for i in tqdm(range(1, 500)):
  for j in range(-300, 500):
    a, b = calc(x, y, [i, j]) 
    if a is True:
      total += 1
      #ret.append(b)

#print(sorted(ret, reverse=True))
print(total)
