def find_order(element, modulus):
    """
    Find the multiplicative order of an element in Z_n
    Returns the smallest positive integer k such that element^k ≡ 1 (mod modulus)
    """
    if element == 1:
        return 1
   
    # Check if element and modulus are coprime
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
   
    if gcd(element, modulus) != 1:
        raise ValueError(f"{element} and {modulus} are not coprime")
   
    # Find order by trying powers until we get 1
    power = 1
    k = 1
    while True:
        power = (power * element) % modulus
        if power == 1:
            return k
        k += 1


# Calculate ord_11(3)
element = 3
modulus = 11


try:
    order = find_order(element, modulus)
    print(f"The multiplicative order of {element} modulo {modulus} is: {order}")
   
    # Verify the result
    print("\nVerification:")
    for i in range(1, order + 1):
        result = pow(element, i, modulus)
        print(f"{element}^{i} ≡ {result} (mod {modulus})")
       
except ValueError as e:
    print(f"Error: {e}")