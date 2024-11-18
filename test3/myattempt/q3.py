import numpy as np
from math import log2

def calculate_entropy(probabilities):
    """Calculate the entropy of the source"""
    return -sum(p * log2(p) for p in probabilities if p > 0)

def calculate_average_length_convergence(probabilities, n):
    """
    Calculate the average codeword length per symbol for S^n
    
    Parameters:
    probabilities (list): Original source probabilities
    n (int): Extension order
    
    Returns:
    float: Average length per symbol
    """
    # For large n, the average length per symbol converges to the entropy
    # This is a direct result of Shannon's source coding theorem
    H = calculate_entropy(probabilities)
    return H

def calculate_source_probabilities(n):
    """
    Calculate probabilities for S^n based on original probabilities
    Note: For this problem, we only need the entropy as n→∞
    """
    original_probs = [1/2, 1/3, 1/6]
    return original_probs

# Original source probabilities
probabilities = [1/2, 1/3, 1/6]

# Calculate entropy (which is the limit as n→∞)
entropy = calculate_entropy(probabilities)

# Round to 3 decimal places
result = round(entropy, 3)

print(f"Original probabilities: {probabilities}")
print(f"Entropy (H(S)): {entropy}")
print(f"Average codeword length per symbol as n→∞: {result}")

# Verification steps
print("\nVerification:")
print("1. The source coding theorem states that as n→∞, the average length")
print("   per symbol approaches the entropy H(S)")
print(f"2. H(S) = -Σ p_i log2(p_i)")
print("3. Calculating terms:")
for p in probabilities:
    print(f"   -{p} * log2({p}) = {-p * log2(p)}")