import math
from fractions import Fraction

# Transition matrix
M = [[0.55, 0.2], [0.45, 0.8]]

# Equilibrium distribution
P = [Fraction(4, 13), Fraction(9, 13)]

# Calculate binary Markov entropy
H_M = -sum(P[i] * M[i][j] * math.log2(M[i][j]) for i in range(2) for j in range(2))

# Print the result rounded to two decimal places
print(f"Binary Markov entropy (H_M): {H_M:.2f}")
