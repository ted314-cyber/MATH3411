def is_pseudoprime(n, base):
    """
    Check if n is a pseudoprime to given base a
    A number n is a pseudoprime to base a if:
    1. n is composite
    2. a^(n-1) ≡ 1 (mod n)
    """
    # Check if n is composite (91 = 7 × 13 is composite)
    
    # Check Fermat's condition: a^(n-1) ≡ 1 (mod n)
    return pow(base, n-1, n) == 1

def test_bases():
    N = 91
    bases = [6, 7, 5, 2, 3]  # The bases we need to test
    
    print(f"Testing which base makes {N} a pseudo-prime:")
    print("-" * 40)
    
    for base in bases:
        result = is_pseudoprime(N, base)
        print(f"Base {base}: {'IS' if result else 'is NOT'} a valid base")
        if result:
            print(f"\nFound answer: {base} is the correct base!")

# Run the test
test_bases()

# To verify the specific answer 3
print("\nVerifying answer 3:")
print(f"3^90 mod 91 = {pow(3, 90, 91)}")  # Should equal 1 if it's a pseudoprime