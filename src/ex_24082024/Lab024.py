x=int(input("enter x value\n"))
y=int(input("enter y value\n"))

def prob(x,y):

    if x > y:
        print(f"x={x}" " is greater than " f"y={y}")
        res=x-y
        print(f"{res}" " is the difference ")
    else:
        print(f"y={y}" " is greater")
        res1=y-x
        print(f"{res1}" " is the difference")

prob(x,y)