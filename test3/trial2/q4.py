import numpy as np
from scipy.optimize import minimize_scalar

# Entropy function H(x)
def H(x):
    if x == 0 or x == 1:
        return 0
    return -x * np.log2(x) - (1 - x) * np.log2(1 - x)

# Noise entropy H(B | A) as a function of p
def noise_entropy(p):
    return 0.6 * p + 0.3

# Output entropy H(B) as a function of p
def output_entropy(p):
    return H(0.5 * p + 0.2)

# Mutual information I(A; B) = H(B) - H(B | A)
def mutual_information(p):
    return output_entropy(p) - noise_entropy(p)

# Maximize I(A; B) to find the channel capacity
result = minimize_scalar(lambda p: -mutual_information(p), bounds=(0, 1), method='bounded')
optimal_p = result.x
channel_capacity = mutual_information(optimal_p)

print("Optimal value of p:", round(optimal_p, 2))
print("Channel capacity C(A, B):", round(channel_capacity, 4))
