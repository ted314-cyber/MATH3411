import numpy as np
from scipy.optimize import minimize_scalar

def H(x):
    # Binary entropy function with numerical stability for x close to 0 or 1
    x = np.clip(x, 1e-10, 1 - 1e-10)  # Avoid log(0)
    return -x * np.log2(x) - (1 - x) * np.log2(1 - x)

def I(p):
    # Mutual information as a function of p
    return H(0.4 * p + 0.2) - (0.6 * p + 0.1)

# Minimize the negative mutual information to find the maximum
result = minimize_scalar(lambda p: -I(p), bounds=(0, 1), method='bounded')

p_opt = result.x

print(f"Optimal p: {p_opt:.2f}")
