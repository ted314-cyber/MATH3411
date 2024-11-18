def lz78_encode(message):
    dictionary = {}  # Initialize the dictionary
    output = []     # List to store the output pairs
    current_string = ""
    index = 1       # Start indexing from 1
    
    print("Encoding process:")
    print("---------------")
    
    i = 0
    while i < len(message):
        current_string += message[i]
        print(f"Processing: {current_string}")
        
        # If the current string is not in dictionary
        if current_string not in dictionary:
            # If it's a single character
            if len(current_string) == 1:
                output.append((0, current_string))
            else:
                # Look up the prefix in the dictionary
                prefix = current_string[:-1]
                output.append((dictionary[prefix], current_string[-1]))
                
            # Add new string to dictionary
            dictionary[current_string] = index
            index += 1
            # Reset current string
            current_string = ""
            
        print(f"Dictionary: {dictionary}")
        print(f"Output so far: {output}")
        print("---------------")
        i += 1
        
    # If there's a remaining string that matches an existing dictionary entry
    if current_string:
        if len(current_string) == 1:
            output.append((0, current_string))
        else:
            output.append((dictionary[current_string[:-1]], current_string[-1]))
    
    print("\nFinal encoding:")
    for pair in output:
        print(pair)
    
    return output[-1]

# Test with the given message
message = "aabacabbabbabbbb"
print(f"Message to encode: {message}")
last_pair = lz78_encode(message)
print(f"\nThe last pair is: {last_pair}")