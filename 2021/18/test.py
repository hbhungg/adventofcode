def rightval(lst):
  if isinstance(lst, int):
    x = lst
    print("hello", x)
    return 1 
  else:
    return rightval(lst[-1])

print(rightval([1, 1]))
