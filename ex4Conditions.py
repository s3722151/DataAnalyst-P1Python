# https://www.w3schools.com/python/python_conditions.asp
a = 69
b = 420

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
print("")

# Using And
print("Using AND in conditions")
c = 330
d = 331
print("C") if c > d else print("=") if c == d else print("D")
print("")

# Nested statements
print("Nested statements")
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")