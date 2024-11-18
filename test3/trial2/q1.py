import math
from fractions import Fraction


# Probabilities of the symbols
probabilities = [Fraction(1, 3), Fraction(1, 3), Fraction(2, 9), Fraction(1, 9)]


# Radix (base) for the Shannon-Fano code
radix = 3


# Calculate the expected codeword length
average_codeword_length = sum(p * Fraction(math.ceil(-math.log(p, radix))) for p in probabilities)


print(f"Average codeword length: {average_codeword_length}")