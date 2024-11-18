from heapq import heappush, heappop

# Probabilities of the source symbols
probabilities = [6/13, 3/13, 2/13, 2/13]

def calculate_average_huffman_length(probabilities):
    # Create a priority queue (min-heap) with the given probabilities
    heap = []
    for p in probabilities:
        heappush(heap, (p, 1))  # Each entry is a tuple (probability, codeword length)

    # Huffman encoding process
    while len(heap) > 1:
        # Pop the two smallest probabilities
        (p1, l1) = heappop(heap)
        (p2, l2) = heappop(heap)

        # Combine the probabilities and increase the length of the codewords
        combined_probability = p1 + p2
        combined_length = max(l1, l2) + 1

        # Push the combined probability and updated length back into the heap
        heappush(heap, (combined_probability, combined_length))

    # The remaining element in the heap is the root of the Huffman tree
    # Extract the total probability and the average length
    _, total_length = heappop(heap)

    # Calculate the weighted sum of lengths (average length)
    average_length = sum(p * total_length for p in probabilities)
    return average_length

# Compute the average length
average_length = calculate_average_huffman_length(probabilities)
print(f"The average length of the radix-2 Huffman code is: {average_length}")
