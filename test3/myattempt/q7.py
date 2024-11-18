def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b"""
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    """Calculate Euler's totient function φ(n)"""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result = result * (1 - 1/p)
        p += 1
    if n > 1:
        result = result * (1 - 1/n)
    return int(result)

def is_primitive_root(a, n, factors_of_order):
    """
    Check if a is a primitive root modulo n
    factors_of_order: prime factors of the multiplicative group order
    """
    order = n - 1
    for factor in factors_of_order:
        if pow(a, order // factor, n) == 1:
            return False
    return True

def get_prime_factors(n):
    """Get all prime factors of n"""
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors

def count_primitive_elements_gf125():
    """
    Calculate the number of primitive elements in GF(125)
    GF(125) is a field with 125 = 5^3 elements
    """
    # Order of multiplicative group is 124 = 2^2 * 31
    order = 124
    
    # Get prime factors of the order
    factors = get_prime_factors(order)
    
    # Count primitive elements
    count = 0
    for a in range(1, 125):
        if is_primitive_root(a, 125, factors):
            count += 1
            
    return count

# Calculate and print result
count = count_primitive_elements_gf125()
print(f"Number of primitive elements in GF(125): {count}")

# Verify the result
print("\nVerification:")
print("1. GF(125) is a field with 5^3 elements")
print("2. The multiplicative group has order 124 = 2^2 * 31")
print("3. Number of primitive elements = φ(124) = φ(2^2) * φ(31)")
print(f"4. φ(124) = {euler_totient(124)}")