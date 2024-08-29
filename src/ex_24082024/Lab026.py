num=int(input("enter fibnocci number you want:\n"))

def fibnocci(num):

        a = 0
        b = 1
        print(a,b,end=" ")
        for i in range(2, num+1):
            c=a+b
            print(c,end=" ")
            a = b
            b = c

fibnocci(num)
