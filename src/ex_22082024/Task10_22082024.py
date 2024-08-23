# Task #10 - ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

# number=int(input("Enter the Factor Number"))
# if number==0:
#     print("1")
#
# else:
#     for number in range(1,number+1):
#         print(number*number-1)

n = int(input("Enter the number to find factorial of: "))
res = 1
if n == 0:
    print(1)
else:
    for i in range(1, n + 1):
        res = res * i
    print(f"The factorial of {n} is {res}")

