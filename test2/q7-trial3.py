from fractions import Fraction
from itertools import product
from heapq import heappush, heappop

def calculate_extension_probabilities(p1, p2, extension_length=3):
    """Calculate probabilities for 3rd extension"""
    probabilities = []
    sequences = []
    
    # Generate all possible sequences for 3rd extension
    for seq in product([1, 2], repeat=extension_length):
        prob = Fraction(1, 1)
        for s in seq:
            if s == 1:
                prob *= p1
            else:
                prob *= p2
        probabilities.append((prob, seq))
        sequences.append(seq)
    
    # Sort by probability in descending order
    probabilities.sort(reverse=True)
    return probabilities

def build_radix3_huffman(probabilities):
    """Build radix-3 Huffman code"""
    # Add dummy nodes if needed
    n = len(probabilities)
    if n % 2 != 1:  # Need number of nodes that gives remainder 1 when divided by 2
        probabilities.append((Fraction(0), None))
    
    # Initialize priority queue
    heap = [(prob, i, seq) for i, (prob, seq) in enumerate(probabilities)]
    heap.sort(reverse=True)  # Sort in descending order
    
    # Build codes dictionary
    codes = {}
    while len(heap) > 1:
        group = []
        total_prob = Fraction(0)
        
        # Take up to 3 nodes
        for i in range(min(3, len(heap))):
            if heap:
                prob, idx, seq = heap.pop(0)  # Take from front (highest probability)
                group.append((prob, idx, seq))
                total_prob += prob
                
                # Assign codes
                if seq is not None:
                    prefix = str(i)
                    if seq in codes:
                        codes[seq] = prefix + codes[seq]
                    else:
                        codes[seq] = prefix
        
        # Push combined node back
        heap.append((total_prob, len(heap), None))
        heap.sort(reverse=True)
    
    return codes

def find_codeword_s2s2s2():
    # Given probabilities
    p1 = Fraction(3, 5)
    p2 = Fraction(2, 5)
    
    # Get probabilities for 3rd extension
    probabilities = calculate_extension_probabilities(p1, p2)
    
    # Build Huffman codes
    codes = build_radix3_huffman(probabilities)
    
    # Find codeword for s₂s₂s₂ (2,2,2)
    target = (2, 2, 2)
    
    # Ensure we have enough leading zeros
    codeword = codes.get(target, '')
    while len(codeword) < 3:  # Make sure we have at least 3 digits
        codeword = '0' + codeword
        
    return codeword

# Run and print result
result = find_codeword_s2s2s2()
print(f"Codeword for s₂s₂s₂: {result}")