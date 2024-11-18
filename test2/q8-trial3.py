import heapq
from collections import defaultdict

class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''
        
    def __lt__(self, other):
        # If probabilities are equal, compare symbols to ensure consistent ordering
        if abs(self.prob - other.prob) < 1e-10:
            # Convert symbol to string and compare
            return str(self.symbol) > str(other.symbol)
        return self.prob < other.prob

def build_huffman_codes(probabilities, symbols):
    """
    Build Huffman codes for given probabilities and symbols.
    Ensures consistent ordering when probabilities are equal.
    """
    # Create nodes for each symbol
    nodes = []
    for prob, symbol in zip(probabilities, symbols):
        heapq.heappush(nodes, Node(prob, symbol))
    
    # Build the Huffman tree
    while len(nodes) > 1:
        # Get two nodes with lowest probabilities
        right = heapq.heappop(nodes)  # Higher priority (smaller symbol) goes right
        left = heapq.heappop(nodes)   # Lower priority goes left
        
        # Create internal node with combined probability
        internal = Node(left.prob + right.prob, 
                       f"{left.symbol},{right.symbol}",
                       left=left,
                       right=right)
        
        heapq.heappush(nodes, internal)
    
    # Get root of the tree
    root = nodes[0]
    
    # Generate codes by traversing the tree
    codes = {}
    def generate_codes(node, code=''):
        if node is None:
            return
        
        node.code = code
        
        # If it's a leaf node, store its code
        if node.left is None and node.right is None:
            codes[node.symbol] = code
            return
        
        # Traverse left with '0' and right with '1'
        generate_codes(node.left, code + '0')
        generate_codes(node.right, code + '1')
        
    generate_codes(root)
    return codes

def format_huffman_code(probabilities, symbols, target_symbol):
    """
    Calculate and format Huffman code for the target symbol.
    Returns the code in the required format [code1,code2,code3].
    """
    # Sort probabilities in descending order
    sorted_pairs = sorted(zip(probabilities, symbols), reverse=True)
    sorted_probs, sorted_symbols = zip(*sorted_pairs)
    
    # Calculate Huffman codes
    codes = build_huffman_codes(sorted_probs, sorted_symbols)
    
    # Create the formatted output string
    result = []
    for symbol in symbols:
        if symbol in codes:
            result.append(codes[symbol])
    
    return f"[{','.join(result)}]"

def main():
    # Test with the given problem
    probabilities = [3/10, 1/2, 1/5]  # Second column of transition matrix
    symbols = ['s1', 's2', 's3']
    
    print("Input probabilities:", probabilities)
    print("Input symbols:", symbols)
    
    # Sort and display
    sorted_pairs = sorted(zip(probabilities, symbols), reverse=True)
    sorted_probs, sorted_symbols = zip(*sorted_pairs)
    print("\nSorted probabilities:", sorted_probs)
    print("Sorted symbols:", sorted_symbols)
    
    # Calculate and display result
    result = format_huffman_code(probabilities, symbols, 's2')
    print("\nFormatted Huffman code:", result)

if __name__ == "__main__":
    main()