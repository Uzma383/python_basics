# 1. Importing the math module
import math

# 2. Constants
print("Value of pi:", math.pi)
print("Value of e:", math.e)

# 3. Rounding functions
print("Ceil of 4.3:", math.ceil(4.3))   # smallest integer >= number
print("Floor of 4.7:", math.floor(4.7)) # largest integer <= number
print("Truncate 4.7:", math.trunc(4.7)) # removes decimal part
print("Round 4.7:", round(4.7))         # standard rounding

# 4. Power and Square Root
print("Square root of 16:", math.sqrt(16))
print("5 to the power 3:", math.pow(5, 3)) # returns float
print("Absolute value of -7:", math.fabs(-7))

# 5. Factorials
print("Factorial of 5:", math.factorial(5))

# 6. Logarithms
print("Natural log of 10:", math.log(10))      # base e
print("Log base 10 of 1000:", math.log10(1000))
print("Log base 2 of 8:", math.log2(8))

# 7. Trigonometric functions (angle in radians)
angle = math.pi / 2
print("Sin(pi/2):", math.sin(angle))
print("Cos(pi/2):", math.cos(angle))
print("Tan(pi/4):", math.tan(math.pi/4))

# 8. Inverse Trigonometry
print("asin(1):", math.asin(1))
print("acos(0):", math.acos(0))
print("atan(1):", math.atan(1))

# 9. Hyperbolic functions
print("sinh(0):", math.sinh(0))
print("cosh(0):", math.cosh(0))
print("tanh(0):", math.tanh(0))

# 10. Angular conversion
print("Degrees of pi radians:", math.degrees(math.pi))
print("Radians of 180 degrees:", math.radians(180))

# 11. Other useful functions
print("Minimum of 10, 20, 5:", min(10, 20, 5))
print("Maximum of 10, 20, 5:", max(10, 20, 5))
print("Modf of 7.25 (fractional, integer):", math.modf(7.25))
print("Copysign example:", math.copysign(-5, 1))  # magnitude of first, sign of second
print("Is 4 finite?", math.isfinite(4))
print("Is inf finite?", math.isfinite(math.inf))
print("Is nan?", math.isnan(math.nan))
print("Is 5 positive?", math.isqrt(25))  # integer square root
