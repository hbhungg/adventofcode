with open("input.txt") as f:
  lst = f.readlines()
  lst = lst[0].strip()


for i in range(0, len(lst)-14):
  mark = set(lst[i:i+14])
  if len(mark) == 14:
    print(i, i+14)
    break
