"""
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
power=pow(num1,num2)
sub=num1-num2
mul=num1*num2
sum=num1+num2
div=num1/num2

print("power of num1 to num2 is "f"{power}")
print("subtraction of num1 to num2 is "f"{sub}")
print("multiplication of num1 and num2 is "f"{mul}")
print("sum of num1 and num2 is "f"{sum}")
print("div of num1 and num2 is "f"{div}")



