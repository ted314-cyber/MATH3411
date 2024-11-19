import numpy as np
from sympy import Matrix

# Define the parity check matrix H
H = np.array([
    [1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1]
], dtype=int)

# Message bits (given)
m = np.array([1, 1, 0], dtype=int)

# Initialize the codeword x
x = np.zeros(6, dtype=int)

# Positions of message and check bits (0-based indexing)
message_positions = [1, 4, 5]  # Positions 2, 5, 6
check_positions = [0, 2, 3]    # Positions 1, 3, 4

# Place the message bits into the codeword
x[message_positions] = m

# Extract parts of H corresponding to unknown (check bits) and known (message bits)
H_unknowns = H[:, check_positions]
H_knowns = H[:, message_positions]
x_knowns = x[message_positions]

# Compute the right-hand side of the equations
rhs = (-H_knowns.dot(x_knowns)) % 2

# Manually solve the equations over GF(2)
# Equation 3: x3 = rhs[2]
x3 = rhs[2] % 2

# Equation 2: x2 + x3 = rhs[1] => x2 = (rhs[1] - x3) % 2
x2 = (rhs[1] - x3) % 2

# Equation 1: x0 + x2 = rhs[0] => x0 = (rhs[0] - x2) % 2
x0 = (rhs[0] - x2) % 2

# Assign the check bits
x_unknowns = np.array([x0, x2, x3], dtype=int)
x[check_positions] = x_unknowns

# Output the codeword
print("The codeword x encoding the message m = 110 is:", x)
