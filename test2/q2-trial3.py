def generate_radix4_icode(lengths):
    """
    Generate standard radix-4 I-code (using digits 0,1,2,3)
    
    Args:
        lengths: List of codeword lengths
    Returns:
        List of codewords
    """
    # Create a list of tuples (original_index, length)
    indexed_lengths = list(enumerate(lengths))
    # Sort by length, keeping original indices
    indexed_lengths.sort(key=lambda x: x[1])
    
    codewords = [''] * len(lengths)
    queue = ['']
    
    for original_index, length in indexed_lengths:
        while len(queue[0]) < length:
            code = queue.pop(0)
            queue.extend([code + str(i) for i in range(4)])
        codewords[original_index] = queue.pop(0)
    
    return codewords

# Given codeword lengths from the question
lengths = [1, 1, 2, 3]

# Generate codewords
codewords = generate_radix4_icode(lengths)

# Print all codewords
for i, codeword in enumerate(codewords, 1):
    print(f"s{i}: {codeword}")

# Print the codeword for s4 specifically
print(f"\nThe codeword c4 (for s4) is: {codewords[3]}")