import numpy as np
from itertools import combinations, product

def verify_minimum_distance_general(H, radix=3):
    """
    Calculate minimum distance/weight of a linear code
    
    Parameters:
    H: numpy array - Parity check matrix
    radix: int - Use 2 for binary codes, 3 for ternary codes
    """
    num_columns = H.shape[1]
    
    def check_linear_combination(columns, coeffs):
        selected_cols = H[:, list(columns)]
        result = np.zeros(H.shape[0], dtype=int)
        for col, coeff in zip(selected_cols.T, coeffs):
            result = (result + coeff * col) % radix
        return np.all(result == 0)
    
    for r in range(2, num_columns + 1):
        for cols in combinations(range(num_columns), r):
            for coeffs in product(range(radix), repeat=r):
                if all(c == 0 for c in coeffs):  # Skip if all coefficients are 0
                    continue
                if check_linear_combination(cols, coeffs):
                    return r
    
    return num_columns

# MODIFY THESE PARAMETERS BASED ON THE QUESTION:

# 1. For binary code example:
H_binary = np.array([
    [1,0,0,1,0,1,1],
    [0,1,1,1,1,1,0],
    [0,0,1,0,1,0,0],
    [0,0,0,1,0,0,0]
])
radix = 2  # binary code

# 2. For ternary code example:
H_ternary = np.array([
    [2, 2, 0, 0, 2, 0],
    [1, 0, 0, 2, 2, 2],
    [0, 1, 2, 0, 2, 2]
])
# radix = 3  # ternary code

# CHOOSE WHICH VERSION TO RUN:
H = H_binary  # or H_ternary
# radix = 2    # or 3

# Calculate parameters
min_dist = verify_minimum_distance_general(H, radix)

# Print all relevant parameters - they're all related to min_dist
print(f"Parameters for the {radix}-ary linear code:")
print(f"Minimum distance d(C) or weight w(C): {min_dist}")
print(f"Maximum number of errors that can be detected: {min_dist - 1}")
print(f"Maximum number of errors that can be corrected: {(min_dist - 1) // 2}")