def count_ones(binary_string):
    """Count the number of 1s in a binary string (Hamming weight)."""
    return sum(1 for bit in binary_string if bit == '1')

def calculate_max_correctable_errors(min_weight):
    """
    Calculate maximum number of correctable errors using the formula ⌊(d-1)/2⌋
    where d is the minimum distance (equal to minimum weight in linear codes)
    """
    return (min_weight - 1) // 2

# Given codeword
codeword = "010000100"

# Calculate the Hamming weight (number of 1s)
weight = count_ones(codeword)
print(f"Hamming weight of the codeword: {weight}")

# Calculate maximum correctable errors
max_errors = calculate_max_correctable_errors(weight)
print(f"Maximum number of correctable errors: {max_errors}")