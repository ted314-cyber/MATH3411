# Define the Huffman codes for equilibrium distribution and columns of M
huff_e = {'00': 's1', '1': 's2', '01': 's3'}
huff1 = {'10': 's1', '0': 's2', '11': 's3'}
huff2 = {'1': 's1', '00': 's2', '01': 's3'}
huff3 = {'01': 's1', '00': 's2', '1': 's3'}

# Define the binary string to decode
binary_string = "1100100"

def decode(binary_string, huff_e, huff1, huff2, huff3):
    result = []
    i = 0
    huff_codes = [huff_e, huff1, huff2, huff3]
    current_huff_index = 0
    
    # Add debug printing
    print("Starting decoding process...")
    
    while i < len(binary_string):
        current_huff = huff_codes[current_huff_index]
        remaining = binary_string[i:]
        print(f"\nPosition {i}, Remaining string: {remaining}")
        print(f"Using huffman table {current_huff_index}: {current_huff}")
        
        # Try 1-bit code first
        if i + 1 <= len(binary_string):
            code1 = binary_string[i:i+1]
            if code1 in current_huff:
                result.append(current_huff[code1])
                print(f"Found 1-bit code {code1} -> {current_huff[code1]}")
                i += 1
                current_huff_index = (current_huff_index + 1) % 4
                continue
        
        # Then try 2-bit codes
        if i + 2 <= len(binary_string):
            code2 = binary_string[i:i+2]
            if code2 in current_huff:
                result.append(current_huff[code2])
                print(f"Found 2-bit code {code2} -> {current_huff[code2]}")
                i += 2
                current_huff_index = (current_huff_index + 1) % 4
                continue
                
        # If no valid code found, move to next position
        print(f"No valid code found at position {i}")
        i += 1
        
    return ''.join(result)

# Decode the binary string
decoded_string = decode(binary_string, huff_e, huff1, huff2, huff3)

# Display the result
print(f"\nFinal decoded sequence: {decoded_string}")