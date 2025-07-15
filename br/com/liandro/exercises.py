from math import sqrt

a = int(input("Insert the 'A' value: "))
b = int(input("Insert the 'B' value: "))
c = int(input("Insert the 'C' value: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Negative delta")
else:
    sqrt_delta = sqrt(delta)
    x1 = (-b + sqrt_delta) / 2 * a
    x2 = (-b - sqrt_delta) / 2 * a

    print("The roots are", x1, "and", x2)