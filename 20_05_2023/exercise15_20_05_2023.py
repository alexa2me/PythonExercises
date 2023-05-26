import math

# Create an algorithm that reads the length of the opposite and adjacent leg of a right triangle
# and calculate the hypotenuse.
# MATH.SQRT
# HYPOTENUSE = SQRT(A²+B²)

length_opposite = float(input('Type the opposite side length: '))
length_adjacent = float(input('Type the adjacent side length: '))

print('The hypotenuse is {:.2f}.'.format(math.sqrt(length_opposite**2+length_adjacent**2)))
print('The hypotenuse is {:.2f}.'.format(math.hypot(length_opposite, length_adjacent)))
