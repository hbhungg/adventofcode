with open("input.txt") as f:
  lst = f.readline().split(",")
  lst = [int(l) for l in lst]

DAYS = 256
fish_day= {}
for i in range(9):
  fish_day[i] = 0
for l in lst:
  if fish_day.get(l) is None:
    fish_day[l] = 1
  else:
    fish_day[l] += 1

for day in range(DAYS):
  #for key in sorted(fish_day):
  #  print("{}".format(fish_day[key]), end=", ")
  #print()
  zeros = fish_day[0]
  for age in range(0, 8):
    fish_day[age] = fish_day[age+1]
  fish_day[6] += zeros
  fish_day[8] = zeros

print(fish_day)
print(sum(fish_day.values()))
