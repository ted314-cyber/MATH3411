def decompose(n):
    """Decompose n-1 into d * 2^s where d is odd"""
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    return d, s


def is_strong_pseudoprime(n, a):
    """Check if n is a strong pseudo-prime to base a"""
    if n % 2 == 0:
        return False
       
    d, s = decompose(n)
   
    # Calculate a^d mod n
    x = pow(a, d, n)
   
    # If a^d ≡ 1 (mod n), n is a strong pseudo-prime
    if x == 1:
        return True
       
    # Check if a^(d*2^r) ≡ -1 (mod n) for some r < s
    for r in range(s):
        if x == n - 1:
            return True
        x = (x * x) % n
       
    return False


# Number to test
N = 9


# Test for each base
bases = [3, 5, 7, 8]


print(f"Testing {N} for strong pseudo-primality:")
for base in bases:
    result = is_strong_pseudoprime(N, base)
    print(f"Base {base}: {'is' if result else 'is not'} a strong pseudo-prime")


# Additional check to confirm N is composite
def is_composite(n):
    return any(n % i == 0 for i in range(2, int(n**0.5) + 1))


print(f"\nVerification that {N} is composite:", is_composite(N))