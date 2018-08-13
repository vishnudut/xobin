
def extract(string):
  a = string.split(" ")
  for x in a:
    if x.isdigit() and check(x):
      print(x)



def check(n):
  for i in n:
    if i == "9":
      return False
  return True

extract("I have 2 numbers 400 and 380")