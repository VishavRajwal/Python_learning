#COMPOUND INTEREST calculator
principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("Enter the Principle Amount: "))
    if principle <= 0:
        print("Principle amount cannot be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the Interest rate: "))
    if rate <= 0:
        print("Interest rate cannot be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time: "))        
    if time <= 0:
        print("Time cannot be less than or equal to zero")

print(f"The principle amount is: {principle}")
print(f"The Interest rate is: {rate}")
print(f"The Time is: {time}")


total = principle * (1 + rate / time)

print(f"Balance after {time} year/'s: {total}")