import numpy as np
from itertools import combinations

def verify_minimum_distance(H):
    """
    Verify minimum distance by checking all possible combinations of columns
    and showing the detailed work.
    """
    num_columns = H.shape[1]
    print("Starting verification process...")
    
    # Try each possible number of columns
    for r in range(2, num_columns + 1):  # Start from 2 as we want non-zero codewords
        print(f"\nChecking combinations of {r} columns:")
        
        # Try all possible combinations of r columns
        for cols in combinations(range(num_columns), r):
            # Get the selected columns
            selected_cols = H[:, list(cols)]
            
            # Print the columns we're checking
            print(f"\nTesting columns {cols}:")
            print("Selected columns:")
            for i, col in enumerate(cols):
                print(f"Column {col}: {H[:, col]}")
            
            # Sum the columns mod 2
            col_sum = np.sum(selected_cols, axis=1) % 2
            print(f"Sum (mod 2): {col_sum}")
            
            # If we found a linear dependency
            if np.all(col_sum == 0):
                print(f"\nFound linear dependency!")
                print(f"These columns sum to zero (mod 2): {cols}")
                print(f"Therefore, the minimum distance is {r}")
                return r
            else:
                print("Not a linear dependency")
    
    return num_columns

# Define the parity check matrix H
H = np.array([
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1]
])

print("Parity check matrix H:")
print(H)
print("\nVerifying minimum distance...")

min_distance = verify_minimum_distance(H)
print(f"\nFinal result: The minimum distance d(C) of the code is {min_distance}")

# Additional verification: show that no smaller combinations work
print("\nVerifying that no smaller combinations work:")
for r in range(2, min_distance):
    print(f"\nChecking that no combination of {r} columns sums to zero:")
    found_dependency = False
    for cols in combinations(range(H.shape[1]), r):
        selected_cols = H[:, list(cols)]
        col_sum = np.sum(selected_cols, axis=1) % 2
        if np.all(col_sum == 0):
            found_dependency = True
            print(f"Found dependency with columns {cols}!")
            break
    if not found_dependency:
        print(f"Confirmed: No linear dependency exists with {r} columns")