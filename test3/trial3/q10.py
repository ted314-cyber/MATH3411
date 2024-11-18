# Define modulus polynomial: x^4 + x + 1
MODULUS = 0b10011  # Binary representation of x^4 + x + 1

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

def find_multiplicative_order(a):
    """Find the multiplicative order of an element in the field."""
    current = a
    order = 1
    while current != 1:
        current = poly_mul(current, a)
        order += 1
    return order

def poly_inverse(a):
    """Find multiplicative inverse using the order of the field."""
    order = find_multiplicative_order(a)
    # For any element a in a finite field, a^(order-1) is its multiplicative inverse
    return poly_pow(a, order - 1)

def poly_div(num, den):
    """Divide polynomials in the finite field."""
    if den == 0:
        raise ValueError("Division by zero")
    den_inv = poly_inverse(den)
    return poly_mul(num, den_inv)

def poly_to_string(p):
    """Convert polynomial to string representation."""
    if p == 0:
        return "0"
    
    terms = []
    for i in reversed(range(4)):
        if p & (1 << i):
            if i == 0:
                terms.append("1")
            elif i == 1:
                terms.append("a")
            else:
                terms.append(f"a^{i}")
    return " + ".join(terms)

# Part 1: Dimension of field is 4 (degree of the polynomial)
print("1. Dimension of F =", 4)

# Part 2: Calculate a^11
a = 0b10  # 'a' corresponds to x
a_pow_11 = poly_pow(a, 11)
print("2. a^11 =", poly_to_string(a_pow_11))

# Part 3: Simplify (a^8 + a^2)/(a^10 + a^4)
a_pow_8 = poly_pow(a, 8)
a_pow_2 = poly_pow(a, 2)
numerator = poly_add(a_pow_8, a_pow_2)

a_pow_10 = poly_pow(a, 10)
a_pow_4 = poly_pow(a, 4)
denominator = poly_add(a_pow_10, a_pow_4)

# Perform the division
result = poly_div(numerator, denominator)

# Find what power of a this equals
power = 1
test = a
while test != result and power < 16:  # 16 is max possible order in GF(2^4)
    power += 1
    test = poly_mul(test, a)

if test == result:
    print(f"3. Simplified fraction = a^{power}")
else:
    print("3. Simplified fraction =", poly_to_string(result))