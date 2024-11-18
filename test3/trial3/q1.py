import math

# Step 1: Define the source symbols and their probabilities
symbols = ['s1', 's2', 's3', 's4']
probabilities = [0.34, 0.32, 0.22, 0.12]

# Step 2: Compute the codeword lengths using the Shannon-Fano formula for radix 3
def compute_codeword_lengths(probabilities, radix):
    codeword_lengths = []
    for p in probabilities:
        l = math.ceil(-math.log(p, radix))
        codeword_lengths.append(l)
    return codeword_lengths

# Step 3: Assign codewords based on the codeword lengths
def assign_codewords(symbols, codeword_lengths, radix):
    codewords = {}
    # Sort symbols by probabilities in decreasing order
    sorted_symbols = [x for _, x in sorted(zip(probabilities, symbols), reverse=True)]
    sorted_lengths = [x for _, x in sorted(zip(probabilities, codeword_lengths), reverse=True)]
    
    # Generate all possible codewords of given lengths
    from itertools import product
    codeword_pool = []
    max_length = max(sorted_lengths)
    digits = [str(i) for i in range(radix)]
    for length in range(1, max_length + 1):
        codeword_pool.extend([''.join(p) for p in product(digits, repeat=length)])
    
    # Assign codewords ensuring the prefix condition
    assigned_codewords = {}
    used_codewords = set()
    index = 0
    for symbol, length in zip(sorted_symbols, sorted_lengths):
        # Find the next available codeword of the required length that doesn't violate the prefix condition
        while True:
            codeword = codeword_pool[index]
            index += 1
            # Check if any existing codeword is a prefix of this codeword or vice versa
            if not any(codeword.startswith(cw) or cw.startswith(codeword) for cw in used_codewords):
                if len(codeword) == length:
                    assigned_codewords[symbol] = codeword
                    used_codewords.add(codeword)
                    break
    return assigned_codewords

# Step 4: Decode the encoded message using the assigned codewords
def decode_message(encoded_message, codewords):
    # Build a reverse mapping from codeword to symbol
    reverse_codewords = {v: k for k, v in codewords.items()}
    decoded_symbols = []
    i = 0
    while i < len(encoded_message):
        # Try to match codewords starting from the current position
        match_found = False
        for length in range(1, max(len(cw) for cw in codewords.values()) + 1):
            if i + length <= len(encoded_message):
                segment = encoded_message[i:i+length]
                if segment in reverse_codewords:
                    decoded_symbols.append(reverse_codewords[segment])
                    i += length
                    match_found = True
                    break
        if not match_found:
            raise ValueError(f"Unable to decode segment starting at position {i}")
    return decoded_symbols

# Main execution
radix = 3  # Ternary code

# Compute codeword lengths
codeword_lengths = compute_codeword_lengths(probabilities, radix)

# Assign codewords
assigned_codewords = assign_codewords(symbols, codeword_lengths, radix)

print("Assigned Codewords:")
for symbol in symbols:
    print(f"{symbol}: {assigned_codewords[symbol]}")

# Encoded message to decode
encoded_message = '011100'

# Decode the message
decoded_symbols = decode_message(encoded_message, assigned_codewords)

# Format the output
decoded_message = ' '.join(decoded_symbols)
print("\nDecoded Message:")
print(decoded_message)
