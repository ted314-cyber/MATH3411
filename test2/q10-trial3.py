def decode_arithmetic_message(value, intervals, max_symbols=10):
    """
    Decode an arithmetic coded message.
    
    Args:
        value (float): The encoded value to decode
        intervals (dict): Dictionary mapping symbols to their intervals
        max_symbols (int): Maximum number of symbols to decode (to prevent infinite loops)
    
    Returns:
        str: The decoded message
    """
    current_value = value
    decoded_message = ""
    
    # Continue decoding until we hit the stop symbol or max length
    while len(decoded_message) < max_symbols:
        # Find which interval contains the current value
        for symbol, (start, end) in intervals.items():
            if start <= current_value < end:
                decoded_message += symbol
                if symbol == '*':  # Stop symbol found
                    return decoded_message
                
                # Calculate new value for next iteration
                # Using the arithmetic coding scaling formula:
                # new_value = (value - lower_bound) / (upper_bound - lower_bound)
                current_value = (current_value - start) / (end - start)
                break
    
    return decoded_message

def main():
    # Define the intervals from the question
    intervals = {
        's1': (0.0, 0.1),
        's2': (0.1, 0.3),
        '*': (0.3, 1.0)
    }
    
    # Value to decode
    value = 0.023
    
    print(f"Decoding value: {value}")
    print(f"Using intervals: {intervals}")
    
    # Decode the message
    decoded = decode_arithmetic_message(value, intervals)
    print(f"\nDecoded message: {decoded}")

if __name__ == "__main__":
    main()