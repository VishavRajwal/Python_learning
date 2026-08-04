#Temperature conversion

Temperature = float(input("Enter the Temperature: "))
unit = input("celcius or fahrenheit? (c or f): ")

if unit == "c":
    temperature = (Temperature * 9/5) + 32
    unit = "F"

elif unit == "f":
    temperature = (Temperature - 32) * 5/9
    unit = "C"

else:
    print(f"{unit} was not invalid")

print(f"Your temperature is: {temperature} {unit}")