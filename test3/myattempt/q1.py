import math


# Probabilities of the symbols
probabilities = [5/9, 1/3, 1/9]


# Calculate the entropy H(S)
entropy = -sum(p * math.log2(p) for p in probabilities)


# Round the result to 3 decimal places
entropy_rounded = round(entropy, 3)


print(f"The average codeword length per symbol converges to: {entropy_rounded} bits")
