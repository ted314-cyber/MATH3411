import numpy as np

# Define the transition matrix M
M = np.array([[0.85, 0.15],
              [0.75, 0.25]])

# Define the equilibrium distribution P
P = np.array([5/6, 1/6])

# Initialize the entropy H_M
H_M = 0

# Calculate H_M
for i in range(len(P)):
    for j in range(len(P)):
        if M[i][j] > 0:  # To avoid log(0)
            H_M -= P[i] * M[i][j] * np.log2(M[i][j])

# Round the result to two decimal places
H_M = round(H_M, 2)

# Output the entropy
print(f"The binary Markov entropy H_M is: {H_M}")
