class FiniteFieldElement:
    modulus = [1, 0, 0, 1, 1]  # Represents the modulus polynomial x^4 + x + 1

    def __init__(self, coeffs):
        """Initialize an element in F_2[x]/<x^4 + x + 1>"""
        # Ensure coefficients are modulo 2 and length is 4
        self.coeffs = [c % 2 for c in coeffs]
        self.coeffs += [0] * (4 - len(self.coeffs))
    
    def __add__(self, other):
        """Add two elements"""
        return FiniteFieldElement([(a + b) % 2 for a, b in zip(self.coeffs, other.coeffs)])
    
    def __sub__(self, other):
        """Subtract two elements (same as addition in Z_2)"""
        return self.__add__(other)
    
    def __mul__(self, other):
        """Multiply two elements modulo x^4 + x + 1"""
        # Multiply polynomials
        result = [0] * 7  # Degree at most 3 + 3 = 6
        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(other.coeffs):
                result[i + j] ^= a & b  # XOR for addition modulo 2
        
        # Reduce modulo modulus polynomial
        modulus_degree = len(self.modulus) - 1
        while len(result) > 4:
            if result[-1] == 1:
                # Subtract modulus polynomial shifted appropriately
                degree_diff = len(result) - len(self.modulus)
                for i in range(len(self.modulus)):
                    result[degree_diff + i] ^= self.modulus[i]
            result.pop()
        
        return FiniteFieldElement(result)
    
    def __eq__(self, other):
        """Check equality of two elements"""
        return self.coeffs == other.coeffs
    
    def __str__(self):
        """Convert to string representation"""
        terms = []
        powers = ['1', 'a', 'a^2', 'a^3']
        for i, c in enumerate(self.coeffs):
            if c == 1:
                terms.append(powers[i])
        return ' + '.join(terms[::-1]) if terms else '0'  # Reverse for correct order
    
    def __repr__(self):
        return self.__str__()