# Home Can you create a Program I will give you number(userinput and print table)
# "{}" String format concept
# User input - num int -> 10, 100, -1, 2, 3.14 -> input
# 9x1 = 9
# 9x2 = 18... till 10

num1=int(input("Enter a number"))
for i in range(1,11):
    print(f"{num1}" "*" f"{i}" " = " f"{num1 * i}")
    i=i+1

num2=int(input("Enter a number"))
j=1
while j<=10:
    print(f"{num2}" "*" f"{j}" " = " f"{num2 * j}")
    j=j+1

num3=int(input("Enter a number"))
def print_table(num3):
    for i in range(1, 11):
        print(f"{num3}" "*" f"{i}" " = " f"{num3 * i}")
        i = i + 1

print_table(num3)