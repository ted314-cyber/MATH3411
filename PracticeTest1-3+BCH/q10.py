# Burst Error Correction for 4-Character 8-bit ASCII Codes

# Given 7-bit ASCII codewords
ascii_codes = {
    'K': '1001011',
    'y': '1111001',
    'O': '1001111',
    'F': '1000110',
    'U': '1010101',
    'V': '1010110',
    'a': '1100001',
    'h': '1101000'
}

# Function to convert 8-bit binary string to ASCII character
def binary_to_char(b):
    return chr(int(b, 2))

# Function to perform bitwise XOR on integers
def xor(a, b):
    return a ^ b

# Received message with a single error
received_codewords = [
    '01010101',  # c1
    '01010110',  # c2
    '01001111',  # c3
    '11001100'   # c4 (check codeword with error)
]

# Convert received codewords to integers
c1 = int(received_codewords[0], 2)
c2 = int(received_codewords[1], 2)
c3 = int(received_codewords[2], 2)
c4_received = int(received_codewords[3], 2)

# Compute expected check codeword
c4_expected = xor(xor(c1, c2), c3)

# Check for error by comparing expected and received check codeword
if c4_received != c4_expected:
    # Error detected
    # Assume error is in one of the codewords
    # Try correcting c4 first
    c4_corrected = c4_expected
    # Verify if corrected c4 matches expected value
    # Since only one error, and data codewords are more critical, we assume error is in c4
    corrected_codewords = [c1, c2, c3]
else:
    # No error detected
    c4_corrected = c4_received
    corrected_codewords = [c1, c2, c3]

# Convert corrected codewords to binary strings
corrected_binaries = [format(codeword, '08b') for codeword in corrected_codewords]

# Convert binary strings to ASCII characters
decoded_message = ''.join([binary_to_char(b) for b in corrected_binaries])

print("Corrected and Decoded Message:", decoded_message)
