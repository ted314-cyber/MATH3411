# Given codeword
x = '0100001100'

# Calculate the weight (number of ones)
weight = x.count('1')

# Compute the error-correcting capability
t = (weight - 1) // 2

# Output the result
print(f"Maximal number of errors that can always be corrected by C: {t}")
