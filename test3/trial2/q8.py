import math

n = 78793

# Step 1: Find the starting value of x
x = math.isqrt(n)
if x * x < n:
    x += 1

# Step 2: Iteratively find x and y such that t = x^2 - n is a perfect square
while True:
    t = x * x - n
    y = math.isqrt(t)
    if y * y == t:
        break
    x += 1

# Step 3: Compute the factors a and b
a = x - y
b = x + y

# Step 4: Calculate b - a
difference = b - a

print(f"Factors of {n} are: a = {a}, b = {b}")
print(f"The value of b - a is: {difference}")
