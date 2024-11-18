import math
from fractions import Fraction

# Transition matrix
M = [[0.25, 0.7], [0.75, 0.3]]

# Equilibrium distribution
P = [Fraction(1000, 2071), Fraction(1071, 2071)]

# Calculate binary Markov entropy
H_M = -sum(P[i] * M[i][j] * math.log2(M[i][j]) for i in range(2) for j in range(2))

# Print the result rounded to two decimal places
print(f"Binary Markov entropy (H_M): {H_M:.2f}")
