def gcd(a, b):
    """Calculate greatest common divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def prime_factors(n):
    """Find prime factors of n"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

def euler_totient(n):
    """Calculate Euler's totient function φ(n)"""
    factors = prime_factors(n)
    unique_factors = set(factors)
    result = n
    for p in unique_factors:
        result *= (1 - 1/p)
    return int(result)

def order_modulo_n(a, n):
    """Calculate multiplicative order of a modulo n"""
    if gcd(a, n) != 1:
        return 0  # Not coprime
    
    phi = euler_totient(n)
    # Get all divisors of phi
    factors = prime_factors(phi)
    unique_factors = set(factors)
    
    # For each prime factor p of φ(n), check if a^(φ(n)/p) ≡ 1 (mod n)
    for p in unique_factors:
        if pow(a, phi // p, n) == 1:
            return 0  # Not primitive
    return phi

def count_primitive_elements(n):
    """Count number of primitive elements in Z_n"""
    phi = euler_totient(n)
    count = 0
    
    # Check each number coprime to n
    for a in range(1, n):
        if gcd(a, n) == 1:
            if order_modulo_n(a, n) == phi:
                count += 1
    
    return count

# Calculate for Z_250
n = 250
count = count_primitive_elements(n)
phi = euler_totient(n)

print(f"Analysis of Z_{n}:")
print(f"φ({n}) = {phi}")
print(f"Number of primitive elements: {count}")

# Optional: Print the primitive elements
print("\nPrimitive elements:")
for a in range(1, n):
    if gcd(a, n) == 1 and order_modulo_n(a, n) == phi:
        print(a, end=" ")
print()