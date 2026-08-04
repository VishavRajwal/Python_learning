#weight conversion 

Weight = float(input("Enter your Weight: "))
unit = input("Kilograms or Pounds? (k or l): ")
if unit == "K":
    Weight = Weight * 2.205
    unit = "Lbs"

elif unit == "L":
    Weight = Weight / 2.205  
    unit = "Kgs"

else:
    print(f"{unit} was not invalid")

print(f"Your weight is: {Weight} {unit}")    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      