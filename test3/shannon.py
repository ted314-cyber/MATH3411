import math

# Define the probabilities
probabilities = [1/3, 1/3, 2/9, 1/9]

# Calculate the codeword lengths and average length
average_length = sum(p * math.ceil(-math.log(p, 3)) for p in probabilities)

# Display the result as a fraction
from fractions import Fraction
average_length_fraction = Fraction(average_length).limit_denominator()

print("The average codeword length is:", average_length_fraction)
