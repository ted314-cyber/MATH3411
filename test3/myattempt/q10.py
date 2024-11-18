def solve_matrix_equation():
    # Retrieve required powers of a
    a_powers = generate_powers()
    a11 = a_powers[11]
    a8 = a_powers[8]
    a13 = a_powers[13]

    # Construct the matrix and vectors
    matrix = [
        [a11, a8],
        [a8, a11]
    ]
    vector = [a13, a8]

    # Unknowns x and y
    unknowns = [None, None]  # Will store the solutions

    # Since the field size is small, we can brute-force all possible values
    elements = [FiniteFieldElement([0, 0, 0, 0]),  # 0
                FiniteFieldElement([1, 0, 0, 0]),  # 1
                FiniteFieldElement([0, 1, 0, 0]),  # a
                FiniteFieldElement([0, 0, 1, 0]),  # a^2
                FiniteFieldElement([0, 0, 0, 1])]  # a^3

    # Extend elements with higher powers
    elements += a_powers[4:15]  # Add powers from a^4 to a^{14}

    # Try all combinations of x and y
    for x_candidate in elements:
        for y_candidate in elements:
            # Compute left-hand side
            lhs0 = matrix[0][0] * x_candidate + matrix[0][1] * y_candidate
            lhs1 = matrix[1][0] * x_candidate + matrix[1][1] * y_candidate
            # Check if lhs matches the vector
            if lhs0 == vector[0] and lhs1 == vector[1]:
                print(f"Solution found:")
                print(f"x = {x_candidate}")
                print(f"y = {y_candidate}\n")

# Call the function to solve the matrix equation
solve_matrix_equation()
