class Node:
    def __init__(self, probability, symbol=None):
        self.probability = probability
        self.symbol = symbol
        self.left = None
        self.right = None
        self.code = ''

def build_huffman_tree(probabilities):
    nodes = [Node(p, f's{i+1}') for i, p in enumerate(probabilities)]
    
    while len(nodes) > 1:
        # Sort nodes by probability in non-increasing order
        nodes = sorted(nodes, key=lambda x: x.probability, reverse=True)
        
        # Take the two nodes with lowest probabilities
        right = nodes.pop()
        left = nodes.pop()
        
        # Create a new internal node
        internal = Node(left.probability + right.probability)
        internal.left = left
        internal.right = right
        
        nodes.append(internal)
    
    return nodes[0]

def assign_codes(node, code=''):
    if node is None:
        return
    
    node.code = code
    
    # Traverse left (add 0)
    assign_codes(node.left, code + '0')
    # Traverse right (add 1)
    assign_codes(node.right, code + '1')

def get_all_codes(node, codes=None):
    if codes is None:
        codes = {}
    
    if node.symbol:
        codes[node.symbol] = node.code
    
    if node.left:
        get_all_codes(node.left, codes)
    if node.right:
        get_all_codes(node.right, codes)
    
    return codes

def solve_huffman_problem():
    # Given that s6's code is 0010, we know it must be one of the less probable symbols
    # In a 7-symbol Huffman tree with non-increasing probabilities, 
    # the least probable symbols will have the longest codes
    
    # Working backwards from s6's code (0010):
    # - It's 4 bits long
    # - For s7 to be determined uniquely:
    #   - s7 must be related to s6 in the tree
    #   - Given non-increasing probability order, s7 must share all but the last bit with s6
    #   - Therefore s7's code must be 0011
    
    return "1"  # The last bit of 0011

# Test the solution
result = solve_huffman_problem()
print(f"The last bit of s7's codeword is: {result}")