import math

def calculate_channel_probabilities():
    # Given probabilities
    P_a1 = 0.64
    P_b1_given_a1 = 0.83
    P_b2_given_a2 = 0.51
    
    # Calculate P(a2)
    P_a2 = 1 - P_a1
    
    # Calculate P(b1|a2) = 1 - P(b2|a2)
    P_b1_given_a2 = 1 - P_b2_given_a2
    
    # Calculate P(b2|a1) = 1 - P(b1|a1)
    P_b2_given_a1 = 1 - P_b1_given_a1
    
    # Calculate P(b1) using law of total probability
    # P(b1) = P(b1|a1)P(a1) + P(b1|a2)P(a2)
    P_b1 = P_b1_given_a1 * P_a1 + P_b1_given_a2 * P_a2
    
    # Calculate P(b2) = 1 - P(b1)
    P_b2 = 1 - P_b1
    
    # Calculate H(B) = -P(b1)log₂P(b1) - P(b2)log₂P(b2)
    H_B = -P_b1 * math.log2(P_b1) - P_b2 * math.log2(P_b2)
    
    # Round all results to 2 decimal places
    P_a2 = round(P_a2, 2)
    P_b1 = round(P_b1, 2)
    P_b2 = round(P_b2, 2)
    H_B = round(H_B, 2)
    
    return P_a2, P_b1, P_b2, H_B

def main():
    P_a2, P_b1, P_b2, H_B = calculate_channel_probabilities()
    
    print("Results (rounded to 2 decimal places):")
    print(f"P(a2) = {P_a2}")
    print(f"P(b1) = {P_b1}")
    print(f"P(b2) = {P_b2}")
    print(f"H(B) = {H_B}")
    
    # Show verification that probabilities sum to 1
    print("\nVerification:")
    print(f"P(a1) + P(a2) = 0.64 + {P_a2} = {0.64 + P_a2}")
    print(f"P(b1) + P(b2) = {P_b1} + {P_b2} = {P_b1 + P_b2}")

if __name__ == "__main__":
    main()