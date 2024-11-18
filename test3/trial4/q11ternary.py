import math

def calculate_ternary_codeword_lengths(probabilities):
    # Calculate the length of each codeword in ternary by rounding up the log3 probability
    return [math.ceil(-math.log(p, 3)) for p in probabilities]

def assign_ternary_codewords(symbols, lengths):
    # Combine symbols and lengths, then sort by length and symbol
    symbol_lengths = list(zip(symbols, lengths))
    symbol_lengths.sort(key=lambda x: (x[1], symbols.index(x[0])))
    
    codewords = {}
    current_code = [0] * max(lengths)  # Start with the maximum length in ternary
    
    for symbol, length in symbol_lengths:
        # Assign the current code to the symbol
        codewords[symbol] = ''.join(map(str, current_code[:length]))
        
        # Increment the code in a ternary manner
        for i in range(length - 1, -1, -1):
            if current_code[i] < 2:  # Ternary (0, 1, 2)
                current_code[i] += 1
                break
            else:
                current_code[i] = 0
    
    return codewords

# Given symbols and probabilities
symbols = ['s1', 's2', 's3', 's4']
probabilities = [0.36, 0.26, 0.22, 0.16]

# Step 1: Calculate codeword lengths for ternary
lengths = calculate_ternary_codeword_lengths(probabilities)

# Step 2: Assign ternary codewords
codewords = assign_ternary_codewords(symbols, lengths)

# Step 3: Encode the message m = s2 s4 s2 s1
message = ['s2', 's4', 's2', 's1']
encoded_message = ''.join([codewords[symbol] for symbol in message])

# Output the encoded message without spaces
print(encoded_message)
