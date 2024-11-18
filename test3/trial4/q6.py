def compute_phi(n):
    """Compute Euler's Totient function φ(n)"""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            # p is a prime factor of n, remove all occurrences of p from n
            while n % p == 0:
                n = n // p
            # Update result
            result -= result // p
        p += 1
    # If n has a prime factor greater than sqrt(n)
    if n > 1:
        result -= result // n
    return result


def mod_exp(a, b, n):
    """Compute a^b mod n using efficient modular exponentiation"""
    return pow(a, b, n)


# Part 1: Calculate φ(65)
n = 77
phi_n = compute_phi(n)
print(f"φ({n}) = {phi_n}")


# Part 2: Calculate 3^65 mod 65 using Euler's Theorem
# Since gcd(3, 65) = 1, we can use Euler's theorem:
# 3^φ(65) ≡ 1 mod 65
# So, 3^65 mod 65 = 3^(65 mod φ(65)) mod 65


# Compute exponent modulo φ(65)
exponent_mod_phi = 77 % phi_n  # 65 % 48 = 17


# Now compute 3^17 mod 65
result = mod_exp(3, exponent_mod_phi, n)
print(f"3^{n} mod {n} = 3^{exponent_mod_phi} mod {n} = {result}")