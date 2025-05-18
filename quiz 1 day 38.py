x=input("Enter a number: ")
try:
  if x=="quit":
    print("You have quit the program")
  else:
    if int(x)<5 or int(x)>9:
      raise ValueError("Value should be between 5 and 9")
    
    else:
      print(x)
except ValueError as e:
  print(e)
