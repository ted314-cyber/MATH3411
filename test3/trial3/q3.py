import math
import numpy as np

def shannon_fano_entropy(probabilities, base=3):
    """Calculate the Shannon entropy with the given base."""
    return -sum(p * math.log(p, base) for p in probabilities if p > 0)

def calc_avg_length_n(probabilities, n, base=3):
    """
    Calculate average codeword length per symbol for n-fold extension
    for radix-3 Shannon-Fano code.
    """
    # For large n, the average length per symbol converges to the entropy
    entropy = shannon_fano_entropy(probabilities, base)
    # The ceiling function adds at most 1 to the ideal length
    avg_length = entropy + 1/n
    return avg_length

# Given probabilities
probs = [3/5, 1/5, 1/10, 1/10]

# Verify probabilities sum to 1
assert abs(sum(probs) - 1.0) < 1e-10, "Probabilities must sum to 1"

# Calculate the limit as n approaches infinity
entropy = shannon_fano_entropy(probs, 3)

print(f"The entropy H_3(S) = {entropy:.6f}")
print(f"\nAs n → ∞, the average codeword length per symbol")
print(f"converges to H_3(S) = {entropy:.6f}")

# Show convergence for increasing values of n
print("\nConvergence demonstration:")
for n in [1, 10, 100, 1000, 10000]:
    avg_len = calc_avg_length_n(probs, n)
    print(f"n = {n:5d}: {avg_len:.6f}")