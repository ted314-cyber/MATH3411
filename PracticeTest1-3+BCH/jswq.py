import numpy as np
from itertools import combinations, product

def verify_minimum_distance_general(H, radix=3):
    """
    Verify minimum distance for a linear code over GF(radix) by checking combinations 
    of columns and their linear combinations.
    
    Parameters:
    H: numpy array - parity check matrix
    radix: int - the base of the code (2 for binary, 3 for ternary, etc.)
    """
    num_columns = H.shape[1]
    print(f"Starting verification process for GF({radix}) code...")
    
    def check_linear_combination(columns, coeffs):
        """Helper function to check if a linear combination of columns equals zero in GF(radix)"""
        selected_cols = H[:, list(columns)]
        # Multiply each column by its coefficient and sum in GF(radix)
        result = np.zeros(H.shape[0], dtype=int)
        for col, coeff in zip(selected_cols.T, coeffs):
            result = (result + coeff * col) % radix
        return np.all(result == 0)
    
    # Try each possible number of columns
    for r in range(2, num_columns + 1):
        print(f"\nChecking combinations of {r} columns:")
        
        # Try all possible combinations of r columns
        for cols in combinations(range(num_columns), r):
            print(f"\nTesting columns {cols}:")
            print("Selected columns:")
            for i, col in enumerate(cols):
                print(f"Column {col}: {H[:, col]}")
            
            # Try all possible non-zero coefficient combinations in GF(radix)
            for coeffs in product(range(radix), repeat=r):
                # Skip if all coefficients are 0
                if all(c == 0 for c in coeffs):
                    continue
                    
                print(f"Testing coefficients {coeffs}")
                
                # Check if this linear combination equals zero
                if check_linear_combination(cols, coeffs):
                    print(f"\nFound linear dependency!")
                    print(f"Columns {cols} with coefficients {coeffs} sum to zero in GF({radix})")
                    print(f"Therefore, the minimum distance is {r}")
                    return r
                else:
                    print(f"Not a linear dependency with coefficients {coeffs}")
    
    return num_columns

# Example usage for ternary code
H_ternary = np.array([
    [2, 0, 2, 2, 0, 0],
    [0, 1, 0, 2, 1, 2],
    [2, 0, 1, 0, 2, 2]
])

print("Testing ternary code (radix=3):")
print("Parity check matrix H:")
print(H_ternary)
min_distance_ternary = verify_minimum_distance_general(H_ternary, radix=3)
print(f"\nFinal result: The minimum distance d(C) of the ternary code is {min_distance_ternary}")

# Example usage for binary code
H_binary = np.array([
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1]
])

print("\nTesting binary code (radix=2):")
print("Parity check matrix H:")
print(H_binary)
min_distance_binary = verify_minimum_distance_general(H_binary, radix=2)
print(f"\nFinal result: The minimum distance d(C) of the binary code is {min_distance_binary}")