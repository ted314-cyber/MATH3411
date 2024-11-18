def calculate_kraft_sum(lengths, radix):
    """
    Calculate the Kraft sum for given lengths and radix
    Sum of (1/radix^length) for all lengths
    """
    return sum(1/(radix**length) for length in lengths)

def solve_for_unknown_length():
    # Given values
    radix = 3
    K = 8/9  # Kraft-McMillan coefficient
    known_lengths = [1, 1, 3, 3, 3]  # Known lengths
    
    # Try values of l from 1 to 10 (reasonable range)
    for l in range(1, 11):
        # Add the test value to known lengths
        test_lengths = known_lengths + [l]
        
        # Calculate Kraft sum
        kraft_sum = calculate_kraft_sum(test_lengths, radix)
        
        # Check if this matches our target K
        if abs(kraft_sum - K) < 1e-10:  # Using small epsilon for float comparison
            print(f"Found solution: l = {l}")
            print(f"Verification:")
            print(f"Lengths: {known_lengths + [l]}")
            print(f"Kraft sum: {kraft_sum}")
            print(f"Target K: {K}")
            return l
    
    print("No solution found in range 1-10")
    return None

def main():
    # Solve for unknown length
    solve_for_unknown_length()
    
if __name__ == "__main__":
    main()