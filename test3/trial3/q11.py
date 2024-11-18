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

def get_field_size():
    """Calculate field size based on polynomial degree."""
    degree = len(bin(MODULUS)[2:]) - 1  # Degree of modulus polynomial
    return 2 ** degree

def get_polynomial_coefficients(value, degree=4):
    """Get coefficients of polynomial representation."""
    coefficients = []
    for i in range(degree):
        coefficients.append(1 if value & (1 << i) else 0)
    return coefficients

# Part 1: Calculate number of vectors
field_size = get_field_size()
print(f"1. Number of vectors in F = {field_size}")

# Part 2: Express a^13 as linear combination
a = 0b10  # 'a' corresponds to x
a_pow_13 = poly_pow(a, 13)
coeffs = get_polynomial_coefficients(a_pow_13)

# Build the linear combination string
terms = []
for i, coeff in enumerate(coeffs):
    if coeff:
        if i == 0:
            terms.append("1")
        elif i == 1:
            terms.append("a")
        else:
            terms.append(f"a^{i}")

linear_combination = " + ".join(reversed(terms)) if terms else "0"
print(f"2. a^13 = {linear_combination}")

# Part 3: Simplify (a^6 + a^12)/(a^3 + a^14)
numerator = poly_add(poly_pow(a, 6), poly_pow(a, 12))
denominator = poly_add(poly_pow(a, 3), poly_pow(a, 14))

# Find multiplicative inverse of denominator
current = denominator
order = 1
while current != 1:
    current = poly_mul(current, denominator)
    order += 1
denominator_inverse = poly_pow(denominator, order - 1)

# Perform division
result = poly_mul(numerator, denominator_inverse)

# Convert result to power of a if possible
power = 1
test = a
found_power = False
while power <= field_size:
    if test == result:
        found_power = True
        break
    test = poly_mul(test, a)
    power += 1

if found_power:
    print(f"3. Simplified fraction = a^{power}")
else:
    coeffs = get_polynomial_coefficients(result)
    terms = []
    for i, coeff in enumerate(coeffs):
        if coeff:
            if i == 0:
                terms.append("1")
            elif i == 1:
                terms.append("a")
            else:
                terms.append(f"a^{i}")
    print(f"3. Simplified fraction = {' + '.join(reversed(terms))}")