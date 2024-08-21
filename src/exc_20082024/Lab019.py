# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

num1 = int(input("Enter Score\n"))
""" 
num2=int(input("Enter num2\n"))
num3=int(input("Enter num3\n"))
num4=int(input("Enter num4\n"))
num5=int(input("Enter num5\n"))
"""

if num1 >= 90 and num1 <= 100:
    print("GRADE A")
elif 80 <= num1 <= 89:
    print("GRADE B")
elif 70 <= num1 <= 79:
    print("GRADE C")
elif num1 >= 60 and num1 <= 69:
    print("GRADE D")
elif num1 >= 100:
    print("Out of Range")
else:
    print("GRADE F")
