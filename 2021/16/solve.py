with open("input.txt") as f:
  lst = f.readlines()[0].strip()

def bi2de(bit):
 return int(bit, 2)

def hex2bi(h):
  retval = bin(int(h, 16))[2:]
  return "0"*(len(h)*4 - len(retval)) + retval

#lst = "8A004A801A8002F478"
#lst = "38006F45291200"
#lst = "EE00D40C823060"
#lst = "620080001611562C8802118E34"
#lst = "C0015000016115A2E0802F182340"
#lst = "A0016C880162017C3686B18A3D4780"
bits = hex2bi(lst)
print(bits)
print(len(lst))
print(len(bits))

total = 0
def parse(bits):
  global total
  #print("t", total)
  version = bits[0:3] 
  type_id = bits[3:6]
  pos = 6
  #print(bits)
  # print("hello", type_id)
  if bi2de(type_id) == 4:
    group = ""
    while True:
      g = bits[pos:pos+5]
      group += g
      pos += 5
      if g[0] == "0":
        break
    ret = (version, type_id, group)
    #print(int(bi2de(version)))
    #print()
    #print("Literal")
    #print(ret, (tuple(map(bi2de, ret))))
    total += int(bi2de(version))
    return version, type_id, group

  else:
    length_id = bits[pos]
    pos += 1
    if bi2de(length_id) == 0:
      sub_len = bits[pos:pos+15] 
      pos += 15
      sub_len_de = bi2de(sub_len) 
      sub_pack = bits[pos:pos+sub_len_de]
      pos += sub_len_de 
      ret = (version, type_id, length_id, sub_len, sub_pack)
      #print(int(bi2de(version)))
      #print()
      #print("Operator, len type 0")
      #print(ret)
      #print(len(sub_pack))
      #print(tuple(map(bi2de, ret)))
      total += int(bi2de(version))
      temp = sub_pack[:]
      #print(len(temp))
      while len(temp) > 10: 
        sub = "".join(parse(temp)) 
        print()
        print("f", temp)
        temp = temp[len(sub):]
        #print(len(sub), len(temp))
        print("s", temp)
      return version, type_id, length_id, sub_len, sub_pack

    elif bi2de(length_id) == 1:
      sub_num = bits[pos:pos+11]   
      pos += 11
      sub_pack = bits[pos:]
      ret = (version, type_id, length_id, sub_num, sub_pack)
      #print()
      #print("Operator, len type 1")
      #print(ret)
      #print(tuple(map(bi2de, ret)))
      #print(int(bi2de(version)))
      total += int(bi2de(version))
      if sub_num == 1:
        parse(sub_pack)
      else:
        temp = sub_pack
        for i in range(bi2de(sub_num)):
          sub = "".join(parse(temp))
          temp = temp[len(sub):]
      return version, type_id, length_id, sub_num, sub_pack

parse(bits)
print(total)
#p = bits
#while True:
#  try:
#    p = parse(p)
#    print(p)
#    m = map(bi2de, p)
#    print(tuple(m))
#    print()
#    if bi2de(p[1]) == 4:
#      break
#    # elif bi2de(p[2]) == 0:
#    p = p[-1]
#  except IndexError:
#    break
