import numpy as np

def solve_linear_system_mod2(A, b):
    # (Function implementation remains the same)
    A = A.copy() % 2
    b = b.copy() % 2
    nrows, ncols = A.shape
    Ab = np.hstack((A, b.reshape(-1,1))) % 2  # Augmented matrix
    rank = 0

    for col in range(ncols):
        pivot_row = None
        for row in range(rank, nrows):
            if Ab[row, col] == 1:
                pivot_row = row
                break
        if pivot_row is None:
            continue
        if pivot_row != rank:
            Ab[[rank, pivot_row]] = Ab[[pivot_row, rank]]
        for row in range(nrows):
            if row != rank and Ab[row, col] == 1:
                Ab[row] = (Ab[row] + Ab[rank]) % 2
        rank += 1

    for row in range(rank, nrows):
        if Ab[row, -1] == 1 and np.all(Ab[row, :-1] == 0):
            raise ValueError("No solution exists for the system.")

    x = np.zeros(ncols, dtype=int)
    for row in reversed(range(rank)):
        pivot_cols = np.where(Ab[row, :-1] == 1)[0]
        if len(pivot_cols) == 0:
            continue
        col = pivot_cols[0]
        x[col] = Ab[row, -1]
        if len(pivot_cols) > 1:
            x[col] = (x[col] - np.dot(Ab[row, pivot_cols[1:]], x[pivot_cols[1:]])) % 2
    return x

def encode_message(H, message_positions, check_positions, m):
    x = np.zeros(H.shape[1], dtype=int)
    x[message_positions] = m

    H_unknowns = H[:, check_positions]
    H_knowns = H[:, message_positions]
    x_knowns = x[message_positions]
    rhs = (-H_knowns.dot(x_knowns)) % 2

    x_unknowns = solve_linear_system_mod2(H_unknowns, rhs)
    x[check_positions] = x_unknowns % 2
    return x

# Corrected Positions
H_new = np.array([
    [1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1]
], dtype=int)

# Correct positions based on the original problem statement
message_positions_new = [1, 4, 5]  # Positions 2, 5, 6 (0-based indexing)
check_positions_new = [0, 2, 3]    # Positions 1, 3, 4 (0-based indexing)

m_new = np.array([1, 1, 0], dtype=int)  # Message bits
x_new = encode_message(H_new, message_positions_new, check_positions_new, m_new)
print("Encoded codeword:", ''.join(map(str, x_new)))
