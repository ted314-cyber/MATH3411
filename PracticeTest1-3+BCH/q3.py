import math

def prime_factors(n):
    """Return prime factors of n"""
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

def get_prime_factors_of_totient(n):
    """Get prime factors of φ(n)"""
    phi = euler_totient(n)
    return list(set(prime_factors(phi)))

def is_primitive_root(a, n, prime_factors_of_totient):
    """Check if a is a primitive root modulo n"""
    phi = euler_totient(n)
    
    # Check if a^((phi)/p) mod n ≠ 1 for all prime factors p of phi
    for p in prime_factors_of_totient:
        if pow(a, phi // p, n) == 1:
            return False
    return True

def count_primitive_roots(n):
    """Count the number of primitive roots modulo n"""
    if n <= 0:
        return 0
        
    # Get prime factors of φ(n)
    prime_factors_of_totient = get_prime_factors_of_totient(n)
    
    # Count primitive roots
    count = 0
    for a in range(1, n):
        if math.gcd(a, n) == 1:  # Only check units
            if is_primitive_root(a, n, prime_factors_of_totient):
                count += 1
                
    return count

# Solve for n = 1250
n = 1250
result = count_primitive_roots(n)
print(f"The number of primitive elements in Z_{n} is: {result}")