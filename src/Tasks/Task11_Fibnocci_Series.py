# Task #11 - ✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

n = int(input("Enter the number of digits you want in fibonacci series: "))
a = 0
b = 1
if n < 0:
    print("invalid input")
else:
    print("Fibonacci sequence is: ")
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c