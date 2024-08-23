i = int(input("enter a factorial number!"))
y = 1
if i == 0:
    print(1)
else:
    for i in range(1, i + 1):
        y = y * i
    print(f"The factorial {i} is : {y}")
