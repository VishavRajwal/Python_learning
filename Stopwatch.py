#STOPWATCH


import time

seconds = int(input("Enter time in seconds: "))
#for x in reversed.range(0, seconds):
for x in range(seconds, 0, -1):
  print(x)

  time.sleep(1)

print("TIME'S UP")
