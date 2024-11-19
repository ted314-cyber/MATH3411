from heapq import heappush, heappop, heapify

class Node:
    def __init__(self, probability, symbol=None):
        self.probability = probability
        self.symbol = symbol
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.probability < other.probability

def build_huffman_tree(probabilities, symbols):
    """Build Huffman tree and return root node."""
    heap = []
    for prob, sym in zip(probabilities, symbols):
        heappush(heap, Node(prob, sym))
    
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        internal = Node(left.probability + right.probability)
        internal.left = left
        internal.right = right
        heappush(heap, internal)
    
    return heap[0]

def calculate_code_lengths(node, current_depth=0, lengths=None):
    """Calculate the length of each code in the Huffman tree."""
    if lengths is None:
        lengths = {}
    
    if node.symbol is not None:  # Leaf node
        lengths[node.symbol] = current_depth
    else:
        calculate_code_lengths(node.left, current_depth + 1, lengths)
        calculate_code_lengths(node.right, current_depth + 1, lengths)
    
    return lengths

def calculate_average_length(probabilities, lengths):
    """Calculate the average length of the Huffman code."""
    return sum(prob * lengths[sym] for prob, sym in zip(probabilities, lengths.keys()))

# Input data
symbols = ['s1', 's2', 's3', 's4']
probabilities = [6/13, 3/13, 2/13, 2/13]

# Build Huffman tree
root = build_huffman_tree(probabilities, symbols)

# Calculate code lengths
code_lengths = calculate_code_lengths(root)

# Calculate average length
avg_length = calculate_average_length(probabilities, code_lengths)

print("Probabilities:")
for sym, prob in zip(symbols, probabilities):
    print(f"{sym}: {prob}")

print("\nCode lengths:")
for sym, length in code_lengths.items():
    print(f"{sym}: {length}")

print(f"\nAverage length: {avg_length}")

# Calculate the fraction representation
def decimal_to_fraction(decimal):
    """Convert decimal to simplified fraction."""
    numerator = int(decimal * 13)  # Multiply by 13 as this is our denominator
    denominator = 13
    return f"{numerator}/{denominator}"

print(f"Average length as fraction: {decimal_to_fraction(avg_length)}")

# Verify that our codes satisfy Kraft's inequality
kraft_sum = sum(2**-length for length in code_lengths.values())
print(f"\nKraft's inequality check (should be ≤ 1): {kraft_sum}")