'''
How to find the greatest common divisor 
with the help of the Euclidean algorithm.

Worked example for Euclid's algorithm, source: Wikipedia
1071 = 2 × 462 + 147
462 = 3 × 147 + 21
147 = 7 × 21 + 0
'''''

# Shortest solotuion with recursion
def gcdRecur(a, b):
    return a if b == 0 else gcdRecur(b, a % b)
# Example
print(gcdRecur(1071, 462))