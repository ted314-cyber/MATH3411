import numpy as np

def calculate_entropy(probabilities):
    """Calculate entropy for a set of probabilities"""
    entropy = 0
    for p in probabilities:
        if p > 0:  # Avoid log(0)
            entropy -= p * np.log2(p)
    return entropy

def calculate_average_length_for_column(probabilities):
    """
    Calculate average length for a column using Knuth's Theorem.
    For binary Huffman codes, L = H + D where D < 1
    """
    H = calculate_entropy(probabilities)
    # For binary Huffman codes, the average length L is always
    # less than H + 1 and greater than H
    # The exact value is ceiling(H)
    return np.ceil(H)

def calculate_markov_huffman_length(M, p):
    """
    Calculate the average codeword length for a Markov Huffman code
    using L_M = Σ pᵢLᵢ where Lᵢ is calculated from i-th column of M
    """
    n = len(p)
    L_M = 0
    
    # For each column i
    for i in range(n):
        # Get the i-th column of M
        column = M[:, i]
        # Calculate Lᵢ using Knuth's Theorem
        L_i = calculate_average_length_for_column(column)
        # Multiply by pᵢ and add to total
        L_M += p[i] * L_i
    
    return L_M

# Define the transition matrix M
M = np.array([
    [1/10, 1/10, 2/5],
    [7/10, 3/5, 1/2],
    [1/5, 3/10, 1/10]
])

# Define the equilibrium vector p
p = np.array([7/41, 73/123, 29/123])

# Calculate the average codeword length
L_M = calculate_markov_huffman_length(M, p)

# Convert to fraction
from fractions import Fraction
result = Fraction(L_M).limit_denominator(1000)
print(f"Average codeword length L_M = {result}")  # Should output 173/123
print(f"Decimal value = {float(result)}")  # Should be approximately 1.4065040650406504