import math

def calculate_codeword_lengths(probabilities):
    return [math.ceil(-math.log2(p)) for p in probabilities]

def assign_canonical_codewords(symbols, lengths):
    # Combine symbols and lengths
    symbol_lengths = list(zip(symbols, lengths))
    # Sort by length, then by symbol (if needed)
    symbol_lengths.sort(key=lambda x: (x[1], symbols.index(x[0])))
    
    codewords = {}
    codeword_value = 0
    current_length = symbol_lengths[0][1]
    
    for symbol, length in symbol_lengths:
        # If length increases, left-shift the codeword value
        if length > current_length:
            codeword_value <<= (length - current_length)
            current_length = length
        # Get binary representation, padded with zeros to match the codeword length
        codeword = format(codeword_value, '0{}b'.format(length))
        codewords[symbol] = codeword
        codeword_value += 1  # Increment codeword value
    
    return codewords

# Given symbols and probabilities
symbols = ['s1', 's2', 's3', 's4']
probabilities = [0.36, 0.26, 0.22, 0.16]

# Step 1: Calculate codeword lengths
lengths = calculate_codeword_lengths(probabilities)

# Step 2: Assign codewords using canonical code assignment
codewords = assign_canonical_codewords(symbols, lengths)

# Step 3: Encode the message m = s4 s4 s4 s1
message = ['s4', 's4', 's4', 's1']
encoded_message = ''.join([codewords[symbol] for symbol in message])

# Output the encoded message without spaces
print(encoded_message)
