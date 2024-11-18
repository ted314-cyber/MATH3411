def fermat_factorization(n):
    # Start with the ceiling of square root of n
    x = int(n ** 0.5) + 1
   
    while True:
        y_square = x * x - n  # Calculate y^2
        y = int(y_square ** 0.5)  # Try to find y
       
        if y * y == y_square:  # Check if y is a perfect square
            # Found the factors
            a = x - y
            b = x + y
            if a >= 2:  # Check if a ≥ 2
                return a, b
        x += 1


# The number to factorize
n = 35581


# Find the factors
a, b = fermat_factorization(n)


print(f"Factors found: a = {a}, b = {b}")
print(f"Verification: {a} × {b} = {a*b}")
print(f"The value of b - a = {b-a}")