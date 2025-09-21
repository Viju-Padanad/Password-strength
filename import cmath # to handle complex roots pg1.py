import cmath   # to handle complex roots

# a) Prompt the user to input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# b) Check if a is zero
if a == 0:
    print("This is not a quadratic equation (a cannot be zero).")
else:
    # c) Calculate discriminant
    d = b**2 - 4*a*c
    print(f"Discriminant (d) = {d}")

    # d) Based on discriminant
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        print("Two distinct real roots:")
        print(f"Root 1 = {root1}")
        print(f"Root 2 = {root2}")
    elif d == 0:
        root = -b / (2*a)
        print("One real root:")
        print(f"Root = {root}")
    else:
        # use cmath for complex numbers
        root1 = (-b + cmath.sqrt(d)) / (2*a)
        root2 = (-b - cmath.sqrt(d)) / (2*a)
        print("Two complex roots:")
        print(f"Root 1 = {root1.real} + {root1.imag}i")
        print(f"Root 2 = {root2.real} + {root2.imag}i")