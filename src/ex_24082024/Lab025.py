num1=int(input("Enter a number"))
def print_table(num1):
    for i in range(1, 11):
        print(f"{num1}" "*" f"{i}" " = " f"{num1 * i}")
        i = i + 1

print_table(num1)



