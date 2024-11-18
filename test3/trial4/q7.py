def euler_phi(n):
    """Compute Euler's Totient function for integer n."""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            # If p divides n, subtract multiples of p
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        # If n is a prime number greater than 2
        result -= result // n
    return result

def number_of_primitive_elements(q):
    """Compute the number of primitive elements in GF(q)."""
    return euler_phi(q - 1)

q = 25  # Field GF(25)
num_primitive_elements = number_of_primitive_elements(q)
print(f"The number of primitive elements in GF({q}) is {num_primitive_elements}")
