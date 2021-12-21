with open("input.txt") as f:
  lst = f.readlines()
  lst = [l.strip() for l in lst]

ss = lst[0]
img = lst[2:]

def pad(img, x, c):
  b = list(c * (len(img) + x*2))
  img = [list(c*x + l + c*x) for l in img]
  # Top
  for i in range(x):
    img.insert(0, b)
  # Bottom
  for i in range(x):
    img.append(b)
  return img

def depad(img, x):
  for i in range(x):
    img.pop()

  for i in range(x):
    img.pop(0)

  for i in img:
    for k in range(x):
      i.pop()
      i.pop(0)
  return img
  
def pprint(img):
  #for i in img:
  #  print(i)
  print(sum([l.count("#") for l in img]))

def s2b(s):
  #print(s)
  s = s.replace("#", "1")
  s = s.replace(".", "0")
  return int(s, 2)

def blank(size):
  ret = []
  for i in range(size):
    ret.append(list("."*size))
  return ret

def en(img, ss, time):
  img = pad(img, time+50, ".")
  img = [list(l) for l in img]
  pprint(img)

  for t in range(time):
    bl = blank(len(img))
    for i in range(1, len(img)-1):
      for j in range(1, len(img)-1):
        bi = ""
        for k in range(-1, 2):
          bi += "".join(img[i+k][j-1:j+2])
          #print(u+i, v+j, img[u+i][v+j])
        bl[i][j] = ss[s2b(bi)]
    bl = depad(bl, 1)
    img = bl
    pprint(img)
      
en(img, ss, 50)
