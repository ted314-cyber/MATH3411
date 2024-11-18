def phi(n):
    """Calculate Euler's Totient Function for integer n."""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            # If p divides n, subtract multiples of p from result
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    # If n is a prime number greater than 2
    if n > 1:
        result -= result // n
    return result

# Calculate phi(51)
n = 51
phi_n = phi(n)
print(f"ϕ({n}) = {phi_n}")

# Now, compute 5^51 mod 51
# Since gcd(5, 51) = 1, we can use Euler's Theorem: 5^ϕ(51) ≡ 1 mod 51
# ϕ(51) = 32, so 5^32 ≡ 1 mod 51

# Therefore, 5^51 ≡ 5^(32 + 19) ≡ (5^32 * 5^19) mod 51
# Since 5^32 ≡ 1 mod 51, we have 5^51 mod 51 ≡ 5^19 mod 51

# Compute 5^19 mod 51 using modular exponentiation
exponent = 19
modulus = 51
base = 5

# Modular exponentiation
result = pow(base, exponent, modulus)
print(f"5^{51} mod {modulus} = {result}")
