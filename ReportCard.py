name = input("enter student's name: ")
roll_no = input("enter student's roll number: ")
standard = input("enter the standard: ")
marks = int(input("enter the marks(out of 100): "))


print("\n================STUDENT'S REPORT CARD==================")
      
print("Name:", name)
print("Roll number:", roll_no)
print("Standard:", standard)
print("Marks:", marks)
print("-----------------------------------------------------------")
if marks <0 or marks >100:
      


      print("invalid marks entered")
elif marks >=90:
    


    print("Grade: A+")
    print("Result: PASS")
    print("Remarks: OUTSTANDING PERFORMANCE")
elif marks >=80:



    print("Grade: A")
    print("Result: PASS")
    print("Remarks: EXCELLENT")
elif marks >=70:



    print("Grade: B")
    print("Result: PASS")
    print("Remarks: VERY GOOD")
elif marks >60:



    print("Grade: C")
    print("Result: PASS")
    print("Remarks: GOOD")
elif marks >50: 
    


    print("Grade: D")
    print("Result: PASS")
    print("Remarks: NEEDS IMPROVEMENT")
elif marks >33:



    print("Grade: E") 
    print("Result: PASS")
    print("Remarks: WORK HARD")
else:
    print("Grade: F")
    print("Result: FAIL")
if marks == 100:
    print("PERFECT SCORE")
elif marks >= 95:
    print("CONGRATULATIONS! YOU ARE A TOPPER, KEEP UP THE HARDWORK")

print("--------------------------------------------------------------------------------")
print("TAHNKS FOR USING THE REPORT CARD PROGRAMME!") 