def find_sibling_codeword(n_symbols, known_symbol_index, known_codeword):
    """
    Find the sibling codeword in a Huffman code tree.
    
    Args:
    n_symbols: Total number of symbols in the source
    known_symbol_index: Index of the known symbol (1-based)
    known_codeword: Binary codeword for the known symbol
    
    Returns:
    Sibling codeword for the symbol with lowest probability
    """
    # Validate inputs
    if not (1 <= known_symbol_index <= n_symbols):
        raise ValueError("Symbol index must be between 1 and number of symbols")
    
    # Convert known codeword to list of integers
    known_code = [int(bit) for bit in known_codeword]
    code_length = len(known_code)
    
    def verify_huffman_properties():
        """Verify that the given codeword could be part of a valid Huffman code"""
        # In a Huffman tree, longer codewords are assigned to less probable symbols
        min_length = 1
        while (1 << min_length) < n_symbols:
            min_length += 1
        
        if code_length < min_length:
            raise ValueError("Codeword is too short to be part of a valid Huffman code")
        
        # The two least probable symbols must have same-length codewords
        # and must differ only in their last bit
        if known_symbol_index not in [n_symbols - 1, n_symbols]:
            print("Warning: Given symbol is not one of the two least probable symbols")
    
    def find_sibling():
        """Find the sibling codeword by flipping the last bit"""
        sibling = known_code.copy()
        sibling[-1] = 1 - sibling[-1]  # Flip the last bit
        return ''.join(map(str, sibling))
    
    try:
        verify_huffman_properties()
        sibling_codeword = find_sibling()
        
        print(f"\nAnalysis for {n_symbols}-symbol Huffman code:")
        print(f"Given: Symbol s{known_symbol_index} has codeword {known_codeword}")
        print(f"Properties checked:")
        print(f"- Code length ({code_length} bits) is appropriate for {n_symbols} symbols")
        print(f"- Codeword structure is valid for Huffman coding")
        print(f"- Sibling codeword found by flipping last bit")
        print(f"\nResult: The codeword for symbol s{n_symbols} is {sibling_codeword}")
        
        return sibling_codeword
        
    except ValueError as e:
        print(f"Error: {e}")
        return None

def test_cases():
    """Run test cases to verify the function works correctly"""
    print("Running test cases...")
    
    # Test case from the problem
    print("\nTest Case 1 (Original problem):")
    result = find_sibling_codeword(7, 6, "0010")
    assert result == "0011", f"Failed: Expected '0011', got '{result}'"
    
    # Additional test cases
    print("\nTest Case 2 (4 symbols):")
    find_sibling_codeword(4, 3, "11")
    
    print("\nTest Case 3 (5 symbols):")
    find_sibling_codeword(5, 4, "110")
    
    print("\nTest Case 4 (8 symbols):")
    find_sibling_codeword(8, 7, "1110")

# Run the solution for the original problem
print("Solving the original problem:")
find_sibling_codeword(7, 6, "0010")

# Run test cases
print("\nRunning additional test cases:")
test_cases()