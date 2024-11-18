import math

# Given probabilities
P_a1 = 0.57
P_b1_given_a1 = 0.88
P_b2_given_a2 = 0.86

# Step 1: Find P(a2)
P_a2 = 1 - P_a1
print(f"P(a2) = {P_a2:.2f}")

# Since P(b1 | a2) is not given directly, we can compute it as:
# P(b1 | a2) = 1 - P(b2 | a2)
P_b1_given_a2 = 1 - P_b2_given_a2

# Similarly, P(b2 | a1) = 1 - P(b1 | a1)
P_b2_given_a1 = 1 - P_b1_given_a1

# Step 2: Compute P(b1)
P_b1 = (P_b1_given_a1 * P_a1) + (P_b1_given_a2 * P_a2)
print(f"P(b1) = {P_b1:.2f}")

# Step 3: Compute P(b2)
P_b2 = (P_b2_given_a1 * P_a1) + (P_b2_given_a2 * P_a2)
print(f"P(b2) = {P_b2:.2f}")

# Step 4: Compute H(B)
def entropy(probabilities):
    """Compute the entropy of a probability distribution."""
    H = 0
    for p in probabilities:
        if p > 0:
            H -= p * math.log2(p)
    return H

H_B = entropy([P_b1, P_b2])
print(f"H(B) = {H_B:.2f} bits")
