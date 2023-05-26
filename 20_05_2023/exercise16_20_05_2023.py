import math

# Create an algorithm that reads an angle and returns the sine, cosine and tangent values.
# MATH.RADIANS, MATH.SIN, MATH.COS, MATH.TAN

angle = int(input('Type the angle: '))

rad = math.radians(angle)
sin = math.sin(rad)
cosine = math.cos(rad)
tangent = math.tan(rad)

print('The sin is {:.2f}°, the cosine is {:.2f}° and the tangent is {:.2f}°.'.format(sin, cosine, tangent))
