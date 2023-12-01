with open("input.txt") as f:
  lst = f.readlines()
  lst = [i.strip() for i in lst]

energies = []
curr_cal = 0

for i in lst:
  if i != '':
    curr_cal += int(i)
  else:
    energies.append(curr_cal)
    curr_cal = 0

energies = sorted(energies, reverse=True)
print(f"part 1: {energies[0]}")
print(f"part 2: {sum(energies[0:3])}")


