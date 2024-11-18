# Define the field size
mod = 3

def poly_mod(p):
    """Reduce a polynomial modulo x^2 + 2x + 2 over Z_3."""
    # Coefficients are in order [constant term, x^1 term, x^2 term, ...]
    # Since we are working with powers up to x^2, higher powers will be reduced
    # using the relation x^2 ≡ -2x - 2 (mod 3), which simplifies in Z_3
    # because -2 ≡ 1 (mod 3)
    while len(p) > 2:
        # Reduce the highest term
        coeff = p.pop()
        # Apply the relation x^2 ≡ a + 1
        if coeff != 0:
            # Update coefficients for x^1 and x^0
            if len(p) >= 2:
                p[-2] = (p[-2] + coeff * 1) % mod  # x^1 term
            else:
                p.insert(0, coeff * 1 % mod)
            if len(p) >= 1:
                p[-1] = (p[-1] + coeff * 1) % mod  # x^0 term
            else:
                p.insert(0, coeff * 1 % mod)
    return p

def multiply_poly(p1, p2):
    """Multiply two polynomials modulo x^2 + 2x + 2 over Z_3."""
    # Initialize result polynomial
    result = [0] * (len(p1) + len(p2) - 1)
    # Multiply polynomials
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] = (result[i + j] + p1[i] * p2[j]) % mod
    # Reduce the result modulo the minimal polynomial
    return poly_mod(result)

def power_poly(base, exponent):
    """Compute the power of a polynomial modulo x^2 + 2x + 2 over Z_3."""
    result = [1]  # Start with polynomial '1'
    for _ in range(exponent):
        result = multiply_poly(result, base)
    return result

def poly_to_string(p):
    """Convert a polynomial to a string representation."""
    terms = []
    variables = ['', 'a']
    for i, coeff in enumerate(p):
        if coeff != 0:
            terms.append(f"{coeff if coeff > 1 else ''}{variables[i]}")
    if not terms:
        return '0'
    return '+'.join(terms)

# Define the base polynomial 'a' as [0, 1], which represents '0 + 1*a'
a = [0, 1]

# Compute a^7
a_power_7 = power_poly(a, 7)

# Ensure coefficients are non-negative and less than mod
a_power_7 = [coeff % mod for coeff in a_power_7]

# Convert the result to string
a_power_7_str = poly_to_string(a_power_7)

print(f"a^7 expressed as a linear combination of 1 and a is: {a_power_7_str}")
