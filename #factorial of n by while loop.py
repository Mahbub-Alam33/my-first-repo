#factorial of n by while loop
n = int(input("enter value of n: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial of n is =",fact)