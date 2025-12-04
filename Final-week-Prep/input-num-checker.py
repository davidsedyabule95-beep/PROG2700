# Long Form 
#print(f"Enter a valid number (1-26),0 to exit:")
#selection = input()

while True:
  try:
  selection = input("Enter a valid number (1-26),0 to exit: ")

  if selection == 0:
     print(f"Thank tyou four using the number checeker.")
     break
  elif 1 <= selection <= 26:
     print(f"Well done")
  else:
     print(f"Invalid input.")
  except ValueError:
     print(f"Invalid input. Please enter a integer.")
     
    
  