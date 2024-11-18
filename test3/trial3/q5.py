def compute_phi(n):
    """Compute Euler's Totient function phi(n)"""
    result = n
    p = 2
    while p * p <= n:
        # Check if p is a prime factor of n
        if n % p == 0:
            # If yes, then remove all occurrences of p from n
            while n % p == 0:
                n = n // p
            # Update result
            result -= result // p
        p += 1
    # If n has a prime factor greater than sqrt(n)
    if n > 1:
        result -= result // n
    return result

# Compute phi(136)
n = 136
phi_n = compute_phi(n)
print(f"The number of units in Z_{n} is {phi_n}.")
