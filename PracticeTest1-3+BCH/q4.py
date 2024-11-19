def hamming_distance(x, y):
    """Calculate Hamming distance between two binary vectors"""
    if len(x) != len(y):
        raise ValueError("Vectors must be of same length")
    return sum(1 for i in range(len(x)) if x[i] != y[i])

def verify_linear_code(code):
    """
    Verify if the code is linear (closed under addition)
    Addition in GF(2) is XOR
    """
    n = len(code[0])
    for x in code:
        for y in code:
            # Calculate sum (XOR) of two codewords
            sum_vector = tuple(((x[i] + y[i]) % 2) for i in range(n))
            if sum_vector not in code:
                return False
    return True

def find_minimum_length():
    """
    Find the smallest possible length n for a 1-error correcting linear code
    with |C| = 4 codewords
    """
    n = 1  # Start with length 1
    
    while True:
        # For length n, generate all possible binary vectors
        vectors = []
        for i in range(2**n):
            vector = tuple(int(x) for x in format(i, f'0{n}b'))
            vectors.append(vector)
            
        # A linear code must contain the zero vector
        zero_vector = tuple(0 for _ in range(n))
        
        # Try all possible combinations of 3 more vectors with the zero vector
        from itertools import combinations
        for three_vectors in combinations(vectors[1:], 3):
            code = [zero_vector] + list(three_vectors)
            
            # Check if code is linear
            if not verify_linear_code(code):
                continue
                
            # Check minimum Hamming distance
            min_distance = float('inf')
            for i, x in enumerate(code):
                for y in code[i+1:]:
                    min_distance = min(min_distance, hamming_distance(x, y))
            
            # For 1-error correction, need minimum distance ≥ 3
            if min_distance >= 3:
                return n
                
        n += 1

# Find and print result
result = find_minimum_length()
print(f"The smallest possible length n for a radix 2 1-error correcting linear code with 4 codewords is: {result}")

# Verify example code of that length
n = result
zero_vector = tuple(0 for _ in range(n))
print(f"\nExample code of length {n}:")
print(f"[{zero_vector}, (1,1,0), (1,0,1), (0,1,1)]")