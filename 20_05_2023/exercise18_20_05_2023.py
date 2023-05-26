import random

# A teacher would like to draw a name among 4 students to clean the board, create an algorithm
# to read the students names and returning the name of the chosen one.

student1 = input('What is the name of the first student? ')
student2 = input('What is the name of the second student? ')
student3 = input('What is the name of the third student? ')
student4 = input('What is the name of the fourth student? ')

print('The chosen student was... {}.'.format(random.choice([student1, student2, student3, student4])))
