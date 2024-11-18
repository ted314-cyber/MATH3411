from math import gcd

# Given modulus
n = 22

# Step 1: Identify the units in Z_22
units = [x for x in range(1, n) if gcd(x, n) == 1]

# Step 2: Calculate φ(n) and φ(φ(n))
phi_n = len(units)  # Since φ(n) is the number of units modulo n
# Alternatively, φ(22) = φ(2 * 11) = (2 - 1) * (11 - 1) = 10
phi_phi_n = sum(1 for k in range(1, phi_n) if gcd(k, phi_n) == 1)  # φ(φ(n))

# Given that 7 is a primitive element
g = 7

# Step 3: Find all k such that gcd(k, φ(n)) == 1
k_values = [k for k in range(1, phi_n) if gcd(k, phi_n) == 1]

# Compute g^k mod n for each such k to find primitive elements
primitive_elements = set()
for k in k_values:
    element = pow(g, k, n)
    primitive_elements.add(element)

# Convert the set to a sorted list
primitive_elements = sorted(primitive_elements)

# Step 4: Output the primitive elements in the required format
print(f"Primitive elements of Z_{n}^*: {primitive_elements}")
