with open("input.txt") as f:
  lines = f.readlines()
  lines = [l.strip() for l in lines]

calls = lines[0]

total = []
board = []
total_track = []
board_track = []
for i in range(2, len(lines)):
  l = lines[i]
  if l != '':
    board.append(l.split())
    board_track.append([False]*5)
  elif l == '':
    total.append(board)
    total_track.append(board_track)
    board = []
    board_track = []
    
def check(ls):
  for l in ls:
    if sum(l) == 5:
      return True
  for i in range(5):
    if sum([ls[j][i] for j in range(5)]) == 5:
      return True
  return False

test = [[True, False, False, False, False]]*5
#print(test)
#print(check(test))
run = True
calls = calls.split(",")
board_win = [False]*len(total)
print(board_win)
for c in calls:
  for bdx, b in enumerate(total):
    for ldx, l in enumerate(b):
      try:
        total_track[bdx][ldx][l.index(c)] = True
      except:
        pass
    #print((total_track[bdx]))  
    if check(total_track[bdx]) is True and board_win[bdx] is False:
      board_win[bdx] = True
      unmark = 0
      for i in range(5):
        for j in range(5):
          if total_track[bdx][i][j] is False:
            unmark +=int(total[bdx][i][j])
      print(int(c) * unmark)
