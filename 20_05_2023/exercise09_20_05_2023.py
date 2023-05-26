# Create a program that reads a wall width and height, calculate the area and the amount of paint to paint it
# Each liter of paint can cover 2m² of area

width = float(input('What is the wall width? '))
height = float(input('What is the wall height? '))

area = width*height

print('The wall area is {:.2f}m² and about {:.2f}L are needed to paint the whole wall.'.format(area, area/2))


