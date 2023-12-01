with open("input.txt") as f:
  lst = f.readlines()
  lst = [i.strip() for i in lst]

t = 0
t2 = 0
for i in lst:
  p1, p2 = i.split(",")
  p1 = [int(i) for i in p1.split("-")]
  p2 = [int(i) for i in p2.split("-")]
  if p1[0] <= p2[0] and p2[1] <= p1[1]:
    t += 1
  elif p2[0] <= p1[0] and p1[1] <= p2[1]:
    t+= 1
  if max(p1[0], p2[0]) <= min(p1[1], p2[1]):
    t2 += 1

print(t, t2)
