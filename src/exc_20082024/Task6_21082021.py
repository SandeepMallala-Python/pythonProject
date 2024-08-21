### Task #7 ✅ Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

l_year1 = int(input("Enter a year\n"))
#l_year=l_year1%4
#print(l_year)
print("Entered year is "f"{l_year1}")

if l_year1%4==0 or l_year1%400==0:
    print(f"{l_year1}" " is a leap year\n")
# elif l_year1%400==0: print(f"{l_year1}" " is a leap year -2nd condition\n")
else:
    print(f"{l_year1}" " is not a leap year")
