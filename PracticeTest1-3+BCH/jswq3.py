import numpy as np

def solve_linear_system_mod2(A, b):
    """
    Solve the linear system A x = b over GF(2).
    Returns a solution x if one exists, otherwise raises an error.
    """
    A = A.copy() % 2
    b = b.copy() % 2
    nrows, ncols = A.shape
    Ab = np.hstack((A, b.reshape(-1,1))) % 2  # Augmented matrix
    rank = 0

    for col in range(ncols):
        # Find a pivot in current column
        pivot_row = None
        for row in range(rank, nrows):
            if Ab[row, col] == 1:
                pivot_row = row
                break
        if pivot_row is None:
            continue  # No pivot in this column
        # Swap rows if necessary
        if pivot_row != rank:
            Ab[[rank, pivot_row]] = Ab[[pivot_row, rank]]
        # Eliminate other rows
        for row in range(nrows):
            if row != rank and Ab[row, col] == 1:
                Ab[row] = (Ab[row] + Ab[rank]) % 2
        rank += 1

    # Check for inconsistency
    for row in range(rank, nrows):
        if Ab[row, -1] == 1 and np.all(Ab[row, :-1] == 0):
            raise ValueError("No solution exists for the system.")

    # Back substitution
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

    # Solve for the check bits
    x_unknowns = solve_linear_system_mod2(H_unknowns, rhs)
    x[check_positions] = x_unknowns % 2
    return x

# Example 1: First code (from the initial problem)
H1 = np.array([
    [1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1]
], dtype=int)
message_positions1 = [1, 4, 5]  # Positions 2, 5, 6
check_positions1 = [0, 2, 3]    # Positions 1, 3, 4
m1 = np.array([1, 1, 0], dtype=int)
x1 = encode_message(H1, message_positions1, check_positions1, m1)
print("First codeword:", ''.join(map(str, x1)))

# Example 2: Second code (from the second problem)
H2 = np.array([
    [1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 1]
], dtype=int)
message_positions2 = [1, 3, 5]  # Positions 2, 4, 6
check_positions2 = [0, 2, 4]    # Positions 1, 3, 5
m2 = np.array([1, 0, 0], dtype=int)
x2 = encode_message(H2, message_positions2, check_positions2, m2)
print("Second codeword:", ''.join(map(str, x2)))
