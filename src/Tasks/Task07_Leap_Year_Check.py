### Task #7 ✅ Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

year=int(input("enter the year"))

if (year%4==0 and year%100!=0) or year%400==0:
    print("It's a Leap Year")
else:
    print("It's not a leap year")