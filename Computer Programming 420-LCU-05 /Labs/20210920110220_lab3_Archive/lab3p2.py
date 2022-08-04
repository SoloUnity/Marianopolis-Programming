weight = float(input("Weight in kg:"))
height = float(input("Height in meter"))
BMI = weight / (height * height)
if BMI > 25:
  print ("High")
elif BMI < 18.5:
  print ("Low")
else:
  print ("Normal")
print (BMI)