"""
Given a positive real number, print its fractional part.
"""
a=float(input("enter a number"))
import math
val = math.modf(a)

print(val)