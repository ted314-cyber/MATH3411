def parse_encoded_message(encoded_string):
    """
    Parse an encoded message string into a list of tuples.
    Example: "(0,c)(1,c)(1,b)" -> [(0,'c'), (1,'c'), (1,'b')]
    
    Args:
        encoded_string: String in format "(index,char)(index,char)..."
    
    Returns:
        List of (index, char) tuples
    """
    # Remove any whitespace
    encoded_string = encoded_string.replace(" ", "")
    
    # Split the string into individual pairs
    pairs = encoded_string.strip("()").split(")(")
    
    # Convert each pair into a tuple
    encoded_pairs = []
    for pair in pairs:
        index_str, char = pair.split(",")
        index = int(index_str)
        encoded_pairs.append((index, char))
    
    return encoded_pairs

def lz78_decode(encoded_pairs):
    """
    Decode a message encoded using the LZ78 algorithm.
    
    Args:
        encoded_pairs: List of tuples where each tuple contains (index, character)
    
    Returns:
        str: Decoded message
    """
    # Initialize dictionary
    dictionary = {}
    current_index = 1
    decoded_message = ""
    
    # Process each encoded pair
    for index, char in encoded_pairs:
        # Build current sequence
        if index == 0:
            current = char
        else:
            current = dictionary[index] + char
            
        # Add to output message
        decoded_message += current
        
        # Add to dictionary
        dictionary[current_index] = current
        current_index += 1
        
    return decoded_message

def main():
    # You can input your encoded message as a string
    encoded_message = input("Enter the encoded message (e.g., (0,c)(1,c)(1,b)): ")
    
    # Parse the input string into pairs
    encoded_pairs = parse_encoded_message(encoded_message)
    
    # Decode the message
    decoded_message = lz78_decode(encoded_pairs)
    print(f"Decoded message: {decoded_message}")

if __name__ == "__main__":
    main()
