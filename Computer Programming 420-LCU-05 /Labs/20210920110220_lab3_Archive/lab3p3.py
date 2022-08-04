n = int(input("Input an integer: "))
p = 2
while p <= (n ** 0.5):
  while (n % p) == 0:
    print (p)
    n = n // p
  if p == 2:
    p = 3
  else:
    p = p + 2
if n > 1:
  print (n)