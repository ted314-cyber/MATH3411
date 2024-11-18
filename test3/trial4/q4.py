import math

def calculate_entropy(p):
    """Calculate entropy for a binary probability where 1-p is the other probability"""
    if p == 0 or p == 1:
        return 0
    return -p * math.log2(p) - (1-p) * math.log2(1-p)

def main():
    # Given probabilities
    P_a1 = 0.69
    P_b1_given_a1 = 0.96
    P_b2_given_a2 = 0.87
    
    # Calculate P(a2)
    P_a2 = 1 - P_a1
    
    # Calculate P(b2|a1) and P(b1|a2)
    P_b2_given_a1 = 1 - P_b1_given_a1
    P_b1_given_a2 = 1 - P_b2_given_a2
    
    # Calculate H(B|a1)
    H_B_given_a1 = calculate_entropy(P_b1_given_a1)
    
    # Calculate H(B|a2)
    H_B_given_a2 = calculate_entropy(P_b1_given_a2)
    
    # Calculate H(B|A)
    H_B_given_A = P_a1 * H_B_given_a1 + P_a2 * H_B_given_a2
    
    # Round results to 2 decimal places
    H_B_given_a1 = round(H_B_given_a1, 2)
    H_B_given_a2 = round(H_B_given_a2, 2)
    H_B_given_A = round(H_B_given_A, 2)
    
    # Print results
    print(f"H(B|a1) = {H_B_given_a1}")
    print(f"H(B|a2) = {H_B_given_a2}")
    print(f"H(B|A) = {H_B_given_A}")

if __name__ == "__main__":
    main()