# Function to check if a year is a leap year
def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False


# Input validation loop
while True:
  try:
    year = int(input("Enter a year: "))
    if year > 0:
      break
    else:
      print("Please enter a valid positive year.")
  except ValueError:
    print("Please enter a valid numeric year.")

# Check if it's a leap year
if is_leap_year(year):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")
