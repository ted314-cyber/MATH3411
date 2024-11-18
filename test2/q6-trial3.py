class HuffmanNode:
    def __init__(self, codeword=None):
        self.left = None
        self.right = None
        self.codeword = codeword
        self.symbols = []

def build_huffman_tree(known_codewords):
    """Build a partial Huffman tree from known codewords"""
    root = HuffmanNode()
    
    # Insert known codewords into tree
    for symbol, codeword in known_codewords.items():
        current = root
        for bit in codeword:
            if bit == '0':
                if not current.left:
                    current.left = HuffmanNode()
                current = current.left
            else:  # bit == '1'
                if not current.right:
                    current.right = HuffmanNode()
                current = current.right
        current.codeword = codeword
        current.symbols.append(symbol)
    
    return root

def find_sibling_codeword(codeword):
    """Find the sibling codeword by flipping the last bit"""
    if not codeword:
        return None
    return codeword[:-1] + ('0' if codeword[-1] == '1' else '1')

def validate_huffman_properties(known_codewords, n_symbols):
    """Validate basic Huffman code properties"""
    # Check all codewords are unique
    if len(set(known_codewords.values())) != len(known_codewords):
        return False
    
    # Check prefix property
    for c1 in known_codewords.values():
        for c2 in known_codewords.values():
            if c1 != c2 and (c1.startswith(c2) or c2.startswith(c1)):
                return False
    
    return True

def find_related_codeword(known_codewords, target_symbol, n_symbols):
    """Find related codeword based on Huffman properties"""
    # Validate input
    if not validate_huffman_properties(known_codewords, n_symbols):
        return "Invalid Huffman code structure"
    
    # For lowest probability symbols (like s7 and s8 in an 8-symbol code)
    # They must be siblings and have the same length
    max_symbol = max(known_codewords.keys(), key=lambda x: int(x[1:]))
    max_symbol_num = int(max_symbol[1:])
    
    if target_symbol == f"s{max_symbol_num-1}" and f"s{max_symbol_num}" in known_codewords:
        # Find sibling of the lowest probability symbol
        sibling = find_sibling_codeword(known_codewords[f"s{max_symbol_num}"])
        return sibling
    
    return "Cannot determine codeword with given information"

# Example usage
def main():
    # Test cases
    test_cases = [
        {
            'known_codewords': {'s8': '1011'},
            'target_symbol': 's7',
            'n_symbols': 8
        },
        # Add more test cases here
        {
            'known_codewords': {'s6': '110'},
            'target_symbol': 's5',
            'n_symbols': 6
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Known codewords: {test['known_codewords']}")
        print(f"Target symbol: {test['target_symbol']}")
        result = find_related_codeword(
            test['known_codewords'],
            test['target_symbol'],
            test['n_symbols']
        )
        print(f"Result: {result}")

if __name__ == "__main__":
    main()

# Specific example for the original question
known_codewords = {'s8': '0011'}
result = find_related_codeword(known_codewords, 's7', 8)
print(f"\nOriginal question result:")
print(f"Given s8 = 0011")
print(f"Computed s7 = {result}")