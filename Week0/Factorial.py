def fact(n):
  fact = 1
  x = 2
  while fact<=n:
    print(fact, end=" ")
    fact = fact*x
    x = x+1

fact(10)