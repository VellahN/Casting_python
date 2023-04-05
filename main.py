myScore = int(input("Your score: "))

if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")

myPL = float(input("What is PL to 3dp?"))
if myPL == 3.142:
  print("Exactly")
else:
  print("Try again")

yearBorn = int(input("What year where you born: "))

if yearBorn >= 1883 and yearBorn <= 1900:
  print("Lost Generation")
elif yearBorn >= 1901 and yearBorn <= 1927:
  print("Greatest Generation")
elif yearBorn >= 1928 and yearBorn <= 1945:
  print("Silent Generation")
elif yearBorn >= 1946 and yearBorn <= 1964:
  print("Baby Booners")
elif yearBorn >= 1965 and yearBorn <= 1980:
  print("Genaration X")
elif yearBorn >= 1981 and yearBorn <= 1996:
  print("Millennials")
elif yearBorn >= 1997 and yearBorn <= 2012:
  print("Generation Z")
elif yearBorn >= 2012 and yearBorn <= 2030:
  print("Generation alpha")
else:
  print("Try again")