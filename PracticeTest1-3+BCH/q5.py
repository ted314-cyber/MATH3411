from fractions import Fraction
import heapq
from itertools import product
from math import gcd

# Define the probabilities of the source symbols
p1 = Fraction(5, 7)
p2 = Fraction(2, 7)

# Generate sequences and their probabilities for the 3rd extension
symbols = ['s1', 's2']
probabilities = {'s1': p1, 's2': p2}
sequences = []
for seq in product(symbols, repeat=3):
    seq_prob = probabilities[seq[0]] * probabilities[seq[1]] * probabilities[seq[2]]
    sequences.append((''.join(seq), seq_prob))

# Add a dummy symbol with zero probability to make the total number of symbols odd
sequences.append(('D', Fraction(0, 1)))  # Dummy symbol

# Sort sequences based on probabilities in increasing order
sequences.sort(key=lambda x: x[1])

# Build the radix-3 Huffman code
class Node:
    def __init__(self, probability, symbols, children=None):
        self.probability = probability
        self.symbols = symbols
        self.children = children or []
    
    def __lt__(self, other):
        return self.probability < other.probability

# Initialize the heap with leaf nodes
heap = [Node(prob, [seq]) for seq, prob in sequences]
heapq.heapify(heap)

# Build the Huffman tree for radix-3
while len(heap) > 1:
    nodes_to_merge = []
    for _ in range(min(3, len(heap))):
        nodes_to_merge.append(heapq.heappop(heap))
    combined_symbols = []
    total_prob = Fraction(0, 1)
    for node in nodes_to_merge:
        combined_symbols.extend(node.symbols)
        total_prob += node.probability
    new_node = Node(total_prob, combined_symbols, nodes_to_merge)
    heapq.heappush(heap, new_node)

# Assign codes to sequences
def assign_codes(node, code=''):
    if node:
        if not node.children:
            # Leaf node
            for symbol in node.symbols:
                code_dict[symbol] = code
        else:
            for idx, child in enumerate(node.children):
                assign_codes(child, code + str(idx))

code_dict = {}
assign_codes(heap[0])

# Calculate the average codeword length
average_length = Fraction(0, 1)
for seq, prob in sequences:
    if prob > 0:
        code_length = len(code_dict[seq])
        average_length += prob * code_length

# Average length per original symbol
average_length_per_symbol = average_length / 3

# Simplify the fraction
numerator = average_length_per_symbol.numerator
denominator = average_length_per_symbol.denominator
common_divisor = gcd(numerator, denominator)
simplified_numerator = numerator // common_divisor
simplified_denominator = denominator // common_divisor

# Output the result
print(f"Average length per original symbol: {simplified_numerator}/{simplified_denominator}")
