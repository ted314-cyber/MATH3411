import numpy as np

def solve_linear_code(H, message, check_bit_positions):
    """
    Solve for a codeword in a binary linear code given:
    - H: parity check matrix
    - message: binary message to encode
    - check_bit_positions: positions of check bits (1-based indexing)
    
    Returns the complete codeword
    """
    # Convert inputs to numpy arrays
    H = np.array(H)
    message = np.array([int(bit) for bit in str(message)])
    
    # Get dimensions
    num_rows, num_cols = H.shape
    
    # Convert check_bit_positions to 0-based indexing
    check_bit_positions = [pos - 1 for pos in check_bit_positions]
    
    # Determine information bit positions (everything not in check bits)
    info_bit_positions = [i for i in range(num_cols) if i not in check_bit_positions]
    
    # Initialize codeword with zeros
    codeword = np.zeros(num_cols, dtype=int)
    
    # Place message bits in their positions
    for msg_idx, pos in enumerate(info_bit_positions):
        if msg_idx < len(message):
            codeword[pos] = message[msg_idx]
    
    # Create system of equations Hx = 0
    # We need to solve for the check bits
    system = []
    results = []
    
    # For each row in H
    for row in H:
        equation = []
        result = 0
        
        # For each check bit position
        for check_pos in check_bit_positions:
            equation.append(row[check_pos])
            
        # Calculate the sum of known terms (info bits)
        for info_pos in info_bit_positions:
            result = (result + row[info_pos] * codeword[info_pos]) % 2
            
        system.append(equation)
        results.append(result)
    
    # Convert to numpy arrays for calculation
    system = np.array(system)
    results = np.array(results)
    
    # Solve the system modulo 2
    # Using Gaussian elimination over GF(2)
    check_bits = solve_mod2(system, results)
    
    # Place check bits in their positions
    for check_bit, pos in zip(check_bits, check_bit_positions):
        codeword[pos] = check_bit
        
    return codeword

def solve_mod2(A, b):
    """
    Solve system of linear equations Ax = b in GF(2)
    using Gaussian elimination
    """
    # Convert to float for calculations
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    
    # Forward elimination
    for i in range(n):
        # Find pivot
        pivot = -1
        for j in range(i, n):
            if A[j][i] == 1:
                pivot = j
                break
                
        if pivot == -1:
            continue
            
        # Swap rows if necessary
        if pivot != i:
            A[i], A[pivot] = A[pivot].copy(), A[i].copy()
            b[i], b[pivot] = b[pivot], b[i]
        
        # Eliminate column
        for j in range(n):
            if i != j and A[j][i] == 1:
                A[j] = (A[j] + A[i]) % 2
                b[j] = (b[j] + b[i]) % 2
    
    # Back substitution
    x = np.zeros(n, dtype=int)
    for i in range(n-1, -1, -1):
        if A[i][i] == 1:
            x[i] = b[i]
            
    return x

# Example usage:
H = [
    [1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1]
]
message = 101
check_bit_positions = [1, 2, 3]  # 1-based indexing

codeword = solve_linear_code(H, message, check_bit_positions)
print(f"Codeword: {''.join(map(str, codeword))}")

# Verify the solution
H = np.array(H)
verification = np.dot(H, codeword) % 2
print(f"Verification (should be all zeros): {verification}")