import math

class Vector:
    def __init__(self, x: float, y: float):
        """Initialize the Vector with x and y components."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two vectors component-wise."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Addition requires another Vector object.")

    def __sub__(self, other):
        """Subtract two vectors component-wise."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Subtraction requires another Vector object.")

    def __mul__(self, other):
        """Multiply vector by a scalar or another vector."""
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("Multiplication requires a scalar (int or float).")

    def __truediv__(self, other):
        """Divide vector by a scalar or another vector."""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return Vector(self.x / other, self.y / other)
        elif isinstance(other, Vector):
            if other.x == 0 or other.y == 0:
                raise ZeroDivisionError("Division by zero in vector components.")
            return Vector(self.x / other.x, self.y / other.y)
        raise TypeError("Division requires a scalar (int or float) or another Vector object.")

    def __eq__(self, other):
        """Check if two vectors are equal."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __gt__(self, other):
        """Compare the magnitude of this vector with another."""
        if isinstance(other, Vector):
            return self.magnitude() > other.magnitude()
        raise TypeError("Comparison requires another Vector object.")

    def __lt__(self, other):
        """Compare the magnitude of this vector with another."""
        if isinstance(other, Vector):
            return self.magnitude() < other.magnitude()
        raise TypeError("Comparison requires another Vector object.")

    def magnitude(self):
        """Calculate the magnitude of the vector."""
        return math.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        """String representation of the vector."""
        return f"Vector({self.x}, {self.y})"

# Example Usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = Vector(0, 1)

print("Addition:", v1 + v2)              # Vector(6, 8)
print("Subtraction:", v1 - v2)           # Vector(-2, -2)
print("Scalar Multiplication:", v1 * 3)  # Vector(6, 9)
print("Scalar Division:", v1 / 2)        # Vector(1.0, 1.5)
print("Element-wise Division:", v1 / v2) # Vector(0.5, 0.6)
print("Equality:", v1 == v2)             # False
print("Greater Than:", v1 > v3)          # True (based on magnitude)
print("Less Than:", v1 < v2)             # True (based on magnitude)

#############################

# Ovelading operators for complex numbers

class ComplexNumber:
    
    def __init__(self , real , imag):
        
        self.real = real
        self.imag = imag

    def __add__(self, other):
        
        if isinstance(other, ComplexNumber):
            
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        
        raise TypeError("Addition requires another ComplexNumber.")

    def __sub__(self, other):
        
        if isinstance(other, ComplexNumber):
            
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        
        raise TypeError("Subtraction requires another ComplexNumber.")

    def __mul__(self, other):
        
        if isinstance(other, ComplexNumber):
            
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            
            return ComplexNumber(real_part, imag_part)
        
        raise TypeError("Multiplication requires another ComplexNumber.")

    def __truediv__(self, other):
        
        if isinstance(other, ComplexNumber):
            
            denominator = other.real**2 + other.imag**2
            
            if denominator == 0:
                
                raise ZeroDivisionError("Cannot divide by zero.")
            
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            
            return ComplexNumber(real_part, imag_part)
        
        raise TypeError("Division requires another ComplexNumber.")

    def __eq__(self, other):
        
        if isinstance(other, ComplexNumber):
            
            return self.real == other.real and self.imag == other.imag
        
        return False

    def __lt__(self, other):
        
        if isinstance(other, ComplexNumber):
            
            return self.magnitude() < other.magnitude()
        
        raise TypeError("Comparison requires another ComplexNumber.")

    def __gt__(self, other):
        
        if isinstance(other, ComplexNumber):
            
            return self.magnitude() > other.magnitude()
        
        raise TypeError("Comparison requires another ComplexNumber.")

    def magnitude(self):
        
        """Calculate the magnitude of the complex number."""
        
        return math.sqrt(self.real**2 + self.imag**2)

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

# Example Usage
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)

# Use overloaded operators
print("Addition:", c1 + c2)         # Output: 3 + 7i
print("Subtraction:", c1 - c2)      # Output: 1 - 1i
print("Multiplication:", c1 * c2)   # Output: -10 + 11i
print("Division:", c1 / c2)         # Output: 0.8235294117647058 - 0.29411764705882354i
print("Equality:", c1 == c2)        # Output: False
print("Greater Than:", c1 > c2)     # Output: False (based on magnitude)
print("Less Than:", c1 < c2)        # Output: True (based on magnitude)