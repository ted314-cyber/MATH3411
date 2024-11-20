def calculate_combinations(n, r):
    """Calculate nCr (binomial coefficient)"""
    if r < 0 or r > n:
        return 0
    
    # Use multiplicative formula for efficiency
    r = min(r, n-r)  # Take advantage of symmetry
    numerator = 1
    denominator = 1
    
    for i in range(r):
        numerator *= (n - i)
        denominator *= (i + 1)
    
    return numerator // denominator

def volume_of_sphere(n, t, q):
    """Calculate the volume of a sphere of radius t in q-ary Hamming space"""
    volume = 0
    for i in range(t + 1):
        # Calculate number of points at distance i
        # Formula: C(n,i) * (q-1)^i
        volume += calculate_combinations(n, i) * ((q-1) ** i)
    return volume

def sphere_packing_bound(n, M, q):
    """
    Find maximum possible t that satisfies the Sphere-Packing Bound
    n: length of code
    M: size of code
    q: radix (base) of code
    Returns: maximum possible t
    """
    # We know that M * V(t) ≤ q^n where V(t) is volume of sphere radius t
    # Try increasing values of t until bound is violated
    t = 0
    while True:
        volume = volume_of_sphere(n, t, q)
        if M * volume > q**n:
            # Bound is violated, return previous valid t
            return t - 1
        t += 1

def min_distance_from_t(t):
    """Calculate minimum distance from error-correction capability"""
    return 2*t + 1

# Parameters from the problem
n = 7        # length of code
M = 28       # size of code |C| = 28
q = 2        # radix (base) 2 code

# Calculate maximum possible t
max_t = sphere_packing_bound(n, M, q)

# Calculate corresponding minimum distance
d = min_distance_from_t(max_t)

print(f"Code parameters:")
print(f"n = {n} (length)")
print(f"M = {M} (size)")
print(f"q = {q} (radix)")
print(f"\nResults:")
print(f"Maximum possible t: {max_t}")
print(f"Greatest possible minimum distance d(C): {d}")

# Verify the bound
V_t = volume_of_sphere(n, max_t, q)
print(f"\nVerification:")
print(f"M * V({max_t}) = {M} * {V_t} = {M * V_t}")
print(f"q^n = {q}^{n} = {q**n}")
print(f"Sphere-Packing Bound satisfied: {M * V_t <= q**n}")