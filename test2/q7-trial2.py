from fractions import Fraction
from heapq import heappush, heappop
from itertools import product

class Node:
    def __init__(self, prob, symbol=None):
        self.prob = prob
        self.symbol = symbol
        self.children = []
        
    def __lt__(self, other):
        return self.prob < other.prob

def calculate_extension_probabilities(p1, p2, extension_length):
    """Calculate probabilities for nth extension"""
    probs = []
    # Generate all possible sequences
    sequences = list(product([1, 2], repeat=extension_length))
    
    # Calculate probability for each sequence
    for seq in sequences:
        prob = Fraction(1, 1)
        for symbol in seq:
            prob *= p1 if symbol == 1 else p2
        probs.append(prob)
    
    return probs

def calculate_radix3_code_lengths(probabilities):
    """Calculate code lengths for radix-3 Huffman code"""
    probs = probabilities.copy()
    
    # Calculate dummy symbols needed
    n = len(probs)
    r = 3
    needed_dummies = (r-1 - ((n-1) % (r-1))) % (r-1)
    print(f"Number of dummy symbols needed: {needed_dummies}")
    
    if needed_dummies > 0:
        probs.extend([Fraction(0)] * needed_dummies)
    
    nodes = []
    for i, prob in enumerate(probs):
        heappush(nodes, Node(prob, i))
    
    while len(nodes) > 1:
        children = []
        total_prob = Fraction(0)
        num_to_combine = min(3, len(nodes))
        
        for _ in range(num_to_combine):
            node = heappop(nodes)
            children.append(node)
            total_prob += node.prob
        
        parent = Node(total_prob)
        parent.children = children
        heappush(nodes, parent)
    
    lengths = {}
    def traverse(node, depth=0):
        if node.symbol is not None:
            lengths[node.symbol] = depth
        for child in node.children:
            traverse(child, depth + 1)
    
    traverse(nodes[0])
    
    return [lengths[i] for i in range(len(probabilities))]

# Calculate for given problem
p1 = Fraction(5, 7)
p2 = Fraction(2, 7)
extension_length = 3

# Get probabilities for 3rd extension
probs = calculate_extension_probabilities(p1, p2, extension_length)
print("\nProbabilities for 3rd extension:")
for i, p in enumerate(probs):
    print(f"Sequence {i+1}: {p}")

# Calculate code lengths
lengths = calculate_radix3_code_lengths(probs)

# Calculate average length per original symbol
# Note: We divide by 3 because each sequence represents 3 original symbols
avg_length_per_symbol = sum(p * l for p, l in zip(probs, lengths)) / 3

print(f"\nAverage length per original symbol: {avg_length_per_symbol}")