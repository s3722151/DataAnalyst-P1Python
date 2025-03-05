# https://www.w3schools.com/python/python_lists.asp

thislist = ["Ratchet", "Clank", "Sly"]
print(thislist)
print(type(thislist))
print("")
print("Now changing the values")
thislist[0:3] = ["blackcurrant", "watermelon"]
for x in thislist:
  print(x)