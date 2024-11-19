import numpy as np

def encode_message(H, check_bit_positions, message):
    """
    Encode a message using a binary linear code.
    
    Parameters:
    H: numpy array - parity check matrix
    check_bit_positions: list - positions of check bits (1-based indexing)
    message: string - binary message to encode
    
    Returns:
    string - encoded codeword
    """
    # Convert check bit positions to 0-based indexing
    check_positions = [pos-1 for pos in check_bit_positions]
    
    # Get dimensions
    n = H.shape[1]  # Length of codeword
    k = n - len(check_positions)  # Length of message
    
    # Convert message to array of integers
    message_bits = np.array([int(bit) for bit in message])
    
    # Initialize codeword with zeros
    codeword = np.zeros(n, dtype=int)
    
    # Find information bit positions (positions that aren't check bits)
    info_positions = [i for i in range(n) if i not in check_positions]
    
    # Place message bits in information positions
    for i, pos in enumerate(info_positions):
        if i < len(message_bits):
            codeword[pos] = message_bits[i]
    
    # Calculate check bits by solving system of equations
    # For each row in H, we need the sum (mod 2) to be 0
    for i, row in enumerate(H):
        # Calculate the sum of products with known bits
        check_sum = sum(row[j] * codeword[j] for j in info_positions) % 2
        
        # If sum is 1, we need to set the corresponding check bit to 1
        # Find which check bit corresponds to this equation
        check_bit_pos = check_positions[i]
        codeword[check_bit_pos] = check_sum
    
    # Convert codeword to string
    return ''.join(str(bit) for bit in codeword)

# Example from the problem
H = np.array([
    [1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1]
])

check_bit_positions = [1, 3, 6]  # Given in problem
message = "1000"  # Given message

print("Parity check matrix H:")
print(H)
print(f"\nCheck bit positions: {check_bit_positions}")
print(f"Message to encode: {message}")

codeword = encode_message(H, check_bit_positions, message)
print(f"\nEncoded codeword: {codeword}")

# Verify that Hx = 0 (mod 2)
x = np.array([int(bit) for bit in codeword])
syndrome = np.dot(H, x) % 2
print("\nVerification:")
print(f"Syndrome (Hx mod 2): {syndrome}")
print(f"Is valid codeword: {np.all(syndrome == 0)}")