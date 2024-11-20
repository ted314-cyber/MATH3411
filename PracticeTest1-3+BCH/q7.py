def poly_add(p1, p2):
    # Add two polynomials over GF(2)
    max_len = max(len(p1), len(p2))
    result = [0]*max_len
    for i in range(max_len):
        a = p1[i] if i < len(p1) else 0
        b = p2[i] if i < len(p2) else 0
        result[i] = (a + b) % 2
    # Remove trailing zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def poly_mul(p1, p2):
    # Multiply two polynomials over GF(2)
    result = [0]*(len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i+j] ^= p1[i]*p2[j]
    # Remove trailing zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def poly_divmod(dividend, divisor):
    # Ensure inputs are mutable lists
    dividend = dividend[:]
    # Remove trailing zeros
    while len(dividend) > 1 and dividend[-1] == 0:
        dividend.pop()
    while len(divisor) > 1 and divisor[-1] == 0:
        divisor.pop()
    
    quotient = [0]*(len(dividend) - len(divisor) + 1)
    while len(dividend) >= len(divisor):
        # Find degree of dividend
        deg_dividend = len(dividend) - 1
        deg_divisor = len(divisor) - 1
        if dividend[-1] == 0:
            dividend.pop()
            continue
        
        deg_diff = deg_dividend - deg_divisor
        quotient[deg_diff] = 1
        
        # Subtract scaled divisor from dividend
        for i in range(len(divisor)):
            if i + deg_diff >= len(dividend):
                break
            dividend[i + deg_diff] ^= divisor[i]
        
        # Remove trailing zeros from dividend
        while len(dividend) > 0 and dividend[-1] == 0:
            dividend.pop()
    
    return quotient, dividend

def encode_message(message_bits):
    # Define the generator polynomials
    m1 = [1, 1, 0, 0, 1]  # x^4 + x^3 + 1
    m3 = [1, 1, 1, 1, 1]  # x^4 + x^3 + x^2 + x + 1
    m = poly_mul(m1, m3)   # m(x) = m1(x)m3(x)
    
    # Create C_I(x) with message bits in positions 8-14
    C_I = [0]*15
    for i in range(7):
        C_I[i + 8] = message_bits[i]
    
    # Calculate C_R(x) = C_I(x) mod m(x)
    _, C_R = poly_divmod(C_I, m)
    
    # Pad C_R with zeros if necessary
    while len(C_R) < 15:
        C_R.append(0)
        
    # Calculate C(x) = C_R(x) + C_I(x)
    codeword = poly_add(C_R, C_I)-0
    # Ensure codeword is exactly 15 bits
    while len(codeword) < 15:
        codeword.append(0)
    
    return codeword[:15]

def decode_message(received):
    # For this simple case, just extract the message bits
    # from positions 8-14 (counting from 0)
    return received[8:15]

# Test encoding
message = [0, 1, 0, 1, 0, 1, 1]  # Original message 0101011
codeword = encode_message(message)
# Convert to string and reverse for display
encoded = ''.join(map(str, codeword[::-1]))
print(f"Encoded codeword: {encoded}")

# Test decoding
received = [int(b) for b in "000010011000110"[::-1]]  # Reverse input
decoded = decode_message(received)
decoded_str = ''.join(map(str, decoded))
print(f"Decoded message: {decoded_str}")