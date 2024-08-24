### Task #8 ✅ Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side1=int(input("enter side 1\n"))
side2=int(input("enter side 2\n"))
side3=int(input("enter side 3\n"))

if side1==side2 and side1==side2 and side2==side3:
    print("equilateral triangle ...!!!")
elif side1==side2 or side1==side3:
    print("isosceles triangle ...!!!")
else:
    print("scalene triangle ...!!!")