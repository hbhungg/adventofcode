with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip().split(" | ") for l in lst]

# Number - signal
# 0 - 6
# 1 - 2 *
# 2 - 5
# 3 - 5
# 4 - 4 *
# 5 - 5
# 6 - 6
# 7 - 3 *
# 8 - 7 * 
# 9 - 6
size = [2, 4, 3, 7]
ret = 0
for i in lst:
  temp = i[1].split(" ")
  for j in temp:
    if len(j) in size:
      ret += 1

print(ret)
retval = 0

for i in lst:
  ret = [1, 7 ,4] + [None] * 6 + [8]
  temp = i[0].split(" ")
  temp = sorted(temp, key= lambda x: len(x))
  top = set(temp[1]) - set(temp[0])
  right_side = temp[0]
  up_left_and_mid = set(temp[2]) - set(temp[1])
  # Finding 2, 3, 5
  for j in range(3, 6):
    if all(item in temp[j] for item in up_left_and_mid):
      ret[j] = 5
    elif all(item in temp[j] for item in right_side):
      ret[j] = 3
    else:
      ret[j] = 2

  # Find 0, 6, 9
  for j in range(6, 9):
    if not all(item in temp[j] for item in up_left_and_mid):
      ret[j] = 0
    elif all(item in temp[j] for item in right_side):
      ret[j] = 9
    else:
      ret[j] = 6
  dd = {}
  for j, k in zip(ret, temp):
    k = " ".join(map(str, sorted(k)))
    dd[k] = j
  out = i[1].split(" ")
  here = 0
  for j in out:
    j = " ".join(map(str, sorted(j)))
    here = here * 10 + dd[j]
     
  retval += here
print(retval)
