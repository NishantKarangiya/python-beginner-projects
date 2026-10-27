print("STUDENT RESULT MANAGEMENT SYSTEM")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = maths + science + english
percentage = total / 3

print("\n--- STUDENT RESULT ---")
print("Name:", name)
print("Total Marks:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")

if percentage >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
    
if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 35:
    print("Grade: D")
else:
    print("Grade: F")
