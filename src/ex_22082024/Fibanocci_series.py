n=int(input("Enter n values for Fibonocci series:\n"))
a=0
b=1


if n<1:
    print("please enter valid no")
else:
    print(a, b, end=" ")
    for i in range(2,n+1):

        c=a+b
        print(c,end=" ")
        a=b
        b=c
