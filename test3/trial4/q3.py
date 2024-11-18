import math
from fractions import Fraction
from itertools import product

def get_prob_third_extension(probs):
    """Generate probabilities for S^3 by calculating products of original probabilities."""
    extension_probs = []
    # Generate all possible combinations of 3 symbols
    for combo in product(range(len(probs)), repeat=3):
        # Calculate probability of this sequence
        prob = 1
        for idx in combo:
            prob *= probs[idx]
        extension_probs.append((combo, prob))
    return sorted(extension_probs, key=lambda x: x[1], reverse=True)

def calc_codeword_length_radix3(prob):
    """Calculate codeword length for radix-3 Shannon-Fano code."""
    if prob == 0:
        return 0
    # For radix-3, use log base 3 and ceiling function
    return math.ceil(-math.log(prob, 3))

def main():
    # Original probabilities
    probs = [Fraction(1, 2), Fraction(3, 10), Fraction(1, 5)]
    
    # Verify probabilities sum to 1
    total = sum(probs)
    assert abs(total - 1) < 1e-10, f"Probabilities sum to {total}, not 1"
    
    # Get probabilities for S^3
    extension_probs = get_prob_third_extension(probs)
    
    # Convert fractions to floats for length calculation
    float_probs = [(seq, float(prob)) for seq, prob in extension_probs]
    
    # Calculate lengths for all sequences
    lengths = []
    for i, (seq, prob) in enumerate(float_probs):
        length = calc_codeword_length_radix3(prob)
        lengths.append((seq, prob, length))
        print(f"Sequence {seq}: Probability = {prob:.6f}, Length = {length}")
    
    # Sort by probability (descending) to find 3rd most likely
    lengths.sort(key=lambda x: x[1], reverse=True)
    
    # Get length of 3rd most likely codeword
    third_most_likely_length = lengths[2][2]
    print(f"\nLength of 3rd most likely codeword: {third_most_likely_length}")

if __name__ == "__main__":
    main()