def is_pseudo_prime(n, base):
    """
    Check if n is a pseudo-prime to given base.
    A number n is pseudo-prime to base a if a^(n-1) ≡ 1 (mod n)
    """
    # First check if base and n are coprime
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    if gcd(base, n) != 1:
        return False
    
    # Check if base^(n-1) ≡ 1 (mod n)
    result = pow(base, n-1, n)
    return result == 1

# Number to test
N = 25

# Test each base
bases = [11, 8, 7, 6, 9]

print(f"Testing N = {N} for pseudo-primality:")
print("-" * 40)

for base in bases:
    is_pseudo = is_pseudo_prime(N, base)
    print(f"Base {base}: {'IS' if is_pseudo else 'is NOT'} a pseudo-prime base")
    print(f"{base}^{N-1} ≡ {pow(base, N-1, N)} (mod {N})")
    print("-" * 40)

# For verification, also show factorization of N
def prime_factors(n):
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

print(f"\nNote: {N} = {' × '.join(map(str, prime_factors(N)))}")