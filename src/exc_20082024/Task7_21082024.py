### Task #8 ✅ Triangle Classifier:
""" Write a program that classifies a triangle based on its side lengths.
    Given three input values representing the lengths of the sides,
    determine if the triangle is equilateral (all sides are equal),
    isosceles (exactly two sides are equal), or scalene (no sides are equal).
    Use an if-else statement to classify the triangle. """
side1=int(input("Enter Side1\n"))
side2=int(input("Enter Side2\n"))
side3=int(input("Enter Side3\n"))

if side1==side2 and side1==side3:
    print("All sides are equal - Equilateral Triangle")
elif (side1==side2 or side1==side3 or side2==side3): 
    print("Exactly Two sides are equal - Isosceles Triangle")
else:
    print("scalene triangle - No sides are equal")