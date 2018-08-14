def thief(a,b):
  if a%2 == 0:
    a = a/2
    return a*b
  else:
    a = (a+1)/2
    return a*b

print(thief(7,15))
  