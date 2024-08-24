### Task #4
# Write a Python program to calculate the area of a circle given its radius using the formula
# ``` area=π×r^2```
#( Take pie as 3.14)

r=int(input("Enter Radius of the circle"))
pi=3.14
area=pi*pow(r,2)
print("Area of the circle is " f"{area}")