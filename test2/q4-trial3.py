from fractions import Fraction
from heapq import heappush, heappop

class Node:
    def __init__(self, prob, symbol=None):
        self.prob = prob
        self.symbol = symbol
        self.children = []
        
    def __lt__(self, other):
        return self.prob < other.prob

def calculate_radix_code_lengths(probabilities):
    """
    Calculate code lengths for a radix-4 Huffman code given a list of probabilities.
    Automatically adds dummy symbols when needed.
    """
    # Convert input probabilities to Fraction objects
    probs = [Fraction(p) if not isinstance(p, Fraction) else p for p in probabilities]
    
    # Calculate number of dummy symbols needed
    n = len(probs)
    r = 3
    needed_dummies = (r-1 - ((n-1) % (r-1))) % (r-1)
    print(f"Number of dummy symbols needed: {needed_dummies}")
    
    # Add dummy symbols with probability 0
    if needed_dummies > 0:
        probs.extend([Fraction(0)] * needed_dummies)
    
    # Create initial nodes
    nodes = []
    for i, prob in enumerate(probs):
        heappush(nodes, Node(prob, i))
    
    # Build the tree by combining 4 nodes at a time (changed from 3)
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
    
    # Get code lengths through tree traversal
    lengths = {}
    def traverse(node, depth=0):
        if node.symbol is not None:  # Leaf node
            lengths[node.symbol] = depth
        for child in node.children:
            traverse(child, depth + 1)
    
    traverse(nodes[0])  # Start from root
    
    # Return lengths only for original symbols (excluding dummies)
    return [lengths[i] for i in range(len(probabilities))]

def verify_average_length(probabilities, code_lengths):
    """
    Verify the average length calculation and show detailed breakdown.
    """
    print("\nCode lengths for each symbol:")
    for i, (prob, length) in enumerate(zip(probabilities, code_lengths)):
        print(f"Symbol {i}: probability = {prob}, length = {length}")
    
    print("\nAverage length calculation:")
    parts = [f"({length} * {prob})" for prob, length in zip(probabilities, code_lengths)]
    print(" + ".join(parts))
    
    average_length = sum(prob * length for prob, length in zip(probabilities, code_lengths))
    print(f"= {average_length}")
    
    return average_length

# Example usage
if __name__ == "__main__":
    # Given probabilities
    probs = [
        Fraction(4, 19), Fraction(4, 19), Fraction(4, 19), Fraction(4, 19),
        Fraction(2, 19), Fraction(1, 19)
    ]
    
    # Calculate code lengths
    lengths = calculate_radix_code_lengths(probs)
    
    # Verify and show results
    avg_length = verify_average_length(probs, lengths)