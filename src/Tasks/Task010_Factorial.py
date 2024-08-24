# Task 10 - ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

fact = int(input("enter fact\n"))
res = 1
if fact == 0 or fact == 1:
    print(1)
else:
    for i in range(1, fact + 1):
        res = res * i
        # i=i+1
        print("The factorial of number " f"{fact} is " f"{res}")
print("The factorial of number " f"{fact} is " f"{res}")
