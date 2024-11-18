# List of possible bases
a_values = [11, 8, 7, 6, 9]

# Composite number N
N = 25

# Iterate over each base a
for a in a_values:
    # Compute a^(N-1) mod N
    result = pow(a, N - 1, N)
    
    # Check if the result is congruent to 1 modulo N
    if result == 1:
        print(f"{a}: N={N} is a pseudoprime to base {a}")
    else:
        print(f"{a}: N={N} is not a pseudoprime to base {a} (Result: {result})")
