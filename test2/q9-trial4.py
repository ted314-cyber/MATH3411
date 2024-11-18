def lz78_encode(message):
    dictionary = {}  # Initialize the dictionary
    output = []     # List to store the output pairs
    current_phrase = ""
    next_index = 1  # Start indexing from 1
    
    print("Encoding process:")
    print("---------------")
    
    i = 0
    while i < len(message):
        current_char = message[i]
        temp_phrase = current_phrase + current_char
        
        print(f"Processing: {temp_phrase}")
        
        # If the new phrase exists in dictionary, extend current phrase
        if temp_phrase in dictionary:
            current_phrase = temp_phrase
        else:
            # Output pair using the current phrase's index (or 0 if empty)
            if current_phrase == "":
                index = 0
            else:
                index = dictionary[current_phrase]
            output.append((index, current_char))
            
            # Add the new phrase to dictionary
            dictionary[temp_phrase] = next_index
            next_index += 1
            
            # Reset current phrase
            current_phrase = ""
            
        print(f"Dictionary: {dictionary}")
        print(f"Output so far: {output}")
        print("---------------")
        i += 1
    
    # Handle any remaining phrase
    if current_phrase:
        output.append((dictionary[current_phrase], ''))
    
    print("\nFinal encoding:")
    for pair in output:
        print(pair)
    
    return output[-1]

# Test with the given message
message = "aabacabbabbabbbb"
print(f"Message to encode: {message}")
last_pair = lz78_encode(message)
print(f"\nThe last pair is: {last_pair}")