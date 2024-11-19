from pyfinite import ffield

def gf2_poly_div(dividend, divisor):
    """
    Perform polynomial division over GF(2).
    """
    dividend = dividend.copy()
    divisor = divisor.copy()
    while divisor and divisor[0] == 0:
        divisor.pop(0)
    if not divisor:
        raise ZeroDivisionError("The divisor polynomial cannot be zero.")
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    while len(dividend) >= len(divisor):
        degree_diff = len(dividend) - len(divisor)
        quotient[degree_diff] = 1
        for i in range(len(divisor)):
            dividend[i + degree_diff] ^= divisor[i]
        while dividend and dividend[0] == 0:
            dividend.pop(0)
    remainder = dividend if dividend else [0]
    return quotient, remainder

def encode_message(message_bits):
    """
    Encode the message using the BCH code.
    """
    codeword = [0]*15
    for i, bit in enumerate(message_bits):
        codeword[14 - i] = bit  # c14 to c8
    # Generator polynomial m(x) = x^8 + x^4 + x^2 + x + 1
    g_coeffs = [1, 0, 0, 0, 1, 0, 1, 1, 1]
    _, remainder = gf2_poly_div(codeword, g_coeffs)
    for i in range(len(remainder)):
        codeword[i] = remainder[i]
    return codeword

def compute_syndromes(received_bits, F):
    """
    Compute syndromes S1, S3, and S5.
    """
    syndromes = []
    n = len(received_bits)
    alpha = 2  # Primitive element
    positions = [i for i, bit in enumerate(received_bits) if bit]
    
    for k in [1, 3, 5]:
        syndrome = 0
        for j in positions:
            exponent = (k * (n - 1 - j)) % 15
            syndrome = F.Add(syndrome, F.Power(alpha, exponent))
        syndromes.append(syndrome)
    return syndromes

def find_error_locator_polynomial(syndromes, F):
    S1, S3, S5 = syndromes
    # Check for no errors
    if S1 == 0 and S3 == 0 and S5 == 0:
        return [1]
        
    # Compute determinant for error pattern analysis
    determinant = F.Subtract(F.Multiply(S1, S1), S3)
    
    if determinant == 0:
        # Single error case
        sigma = [1, S1]
        return sigma
    else:
        # Two errors case
        # Calculate coefficients using syndrome equations
        temp = F.Subtract(F.Multiply(S1, S1), S3)
        if temp == 0:
            raise ValueError("Invalid syndrome pattern")
            
        sigma2 = F.Divide(
            F.Subtract(F.Multiply(S1, S5), F.Multiply(S3, S3)),
            F.Subtract(F.Multiply(S1, S1), S3)
        )
        
        sigma1 = F.Add(S1, F.Multiply(sigma2, S1))
        sigma = [1, sigma1, sigma2]
        return sigma

def find_error_positions(sigma, F):
    """
    Find error positions by finding roots of error locator polynomial.
    """
    alpha = 2  # Primitive element
    roots = []
    for i in range(15):
        x = F.Power(alpha, i)
        result = 0
        for j, coeff in enumerate(sigma):
            term = F.Multiply(coeff, F.Power(x, j))
            result = F.Add(result, term)
        if result == 0:
            roots.append((14 - i) % 15)  # Convert from power to position
    return sorted(roots)

def correct_errors(received_bits, error_positions):
    """
    Correct errors in the received bits at the specified positions.
    """
    corrected_bits = received_bits.copy()
    for pos in error_positions:
        corrected_bits[pos] ^= 1
    return corrected_bits

def main():
    # Message m = 0 1 0 1 0 1 1
    message_bits = [0, 1, 0, 1, 0, 1, 1]
    encoded_codeword = encode_message(message_bits)
    print("Encoded codeword:")
    print(''.join(map(str, encoded_codeword)))

    # Received message with errors
    received_bits = [int(bit) for bit in '000010011000110']
    print("\nReceived message:")
    print(''.join(map(str, received_bits)))

    # Create GF(2^4) with primitive polynomial x^4 + x^3 + 1
    F = ffield.FField(4, gen=0b11001, useLUT=0)

    try:
        # Compute syndromes
        syndromes = compute_syndromes(received_bits, F)
        print("\nSyndromes (S1, S3, S5):")
        print(syndromes)

        # Find error locator polynomial
        sigma = find_error_locator_polynomial(syndromes, F)
        print("\nError locator polynomial coefficients:")
        print(sigma)

        # Find and correct errors
        error_positions = find_error_positions(sigma, F)
        corrected_bits = correct_errors(received_bits, error_positions)
        print("\nCorrected message:")
        print(''.join(map(str, corrected_bits)))
        print("Error positions (0-based index):", error_positions)

        # Extract original message
        decoded_message = corrected_bits[8:15]
        print("\nDecoded message bits:")
        print(''.join(map(str, decoded_message)))
    
    except ValueError as e:
        print("\nDecoding failed:", e)

if __name__ == "__main__":
    main()