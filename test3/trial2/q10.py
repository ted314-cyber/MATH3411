# Define modulus polynomial: x^4 + x^3 + 1
MODULUS = 0b11001  # Binary representation of x^4 + x^3 + 1

def poly_add(a, b):
    """Add two polynomials in GF(2)."""
    return a ^ b

def poly_mul(a, b):
    """Multiply two polynomials modulo the modulus polynomial."""
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        # Reduce modulo the modulus polynomial if degree >= 4
        if a & (1 << 4):
            a ^= MODULUS
    return result

def poly_pow(a, exponent):
    """Raise a polynomial to a power modulo the modulus polynomial."""
    result = 1
    base = a
    while exponent > 0:
        if exponent & 1:
            result = poly_mul(result, base)
        base = poly_mul(base, base)
        exponent >>= 1
    return result

def poly_to_string(p):
    """Convert a polynomial to its string representation."""
    # Check if p equals a^4
    if p == poly_pow(0b10, 4):
        return 'a^4'
    terms = []
    for i in reversed(range(4)):
        if p & (1 << i):
            if i == 0:
                terms.append('1')
            elif i == 1:
                terms.append('a')
            else:
                terms.append(f'a^{i}')
    return ' + '.join(terms) if terms else '0'

# Part 1: Number of vectors
FIELD_SIZE = 2 ** 4  # Since the field is of order 2^4
print(f"1. The field contains {FIELD_SIZE} vectors.")

# Part 2: Compute a^14
a = 0b10  # 'a' corresponds to x
a_pow_14 = poly_pow(a, 14)
print(f"2. a^14 = {poly_to_string(a_pow_14)}")

# Part 3: Simplify (a^11 + a^2) / (a^4 + a^3)
# Compute numerator: a^11 + a^2
a_pow_11 = poly_pow(a, 11)
a_pow_2 = poly_pow(a, 2)
numerator = poly_add(a_pow_11, a_pow_2)

# Compute denominator: a^4 + a^3
a_pow_4 = poly_pow(a, 4)
a_pow_3 = poly_pow(a, 3)
denominator = poly_add(a_pow_4, a_pow_3)

# Since a^4 + a^3 = 1
denominator_poly = denominator
denominator_str = poly_to_string(denominator_poly)
print(f"Denominator (a^4 + a^3) = {denominator_str}")

# Simplify the expression
# Since denominator is 1, the simplified expression is numerator
simplified_expr = numerator

# Since numerator is a^3 + 1 and a^3 + 1 = a^4, update simplified_expr
if simplified_expr == poly_add(a_pow_3, 1):
    simplified_expr = poly_pow(a, 4)

print(f"3. Simplified expression: {poly_to_string(simplified_expr)}")
