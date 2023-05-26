import random

# A teacher would like to draw the order of presentation among 4 students, create an algorithm
# to read the students names and return the drawn order.

student1 = input('What is the name of the first student? ')
student2 = input('What is the name of the second student? ')
student3 = input('What is the name of the third student? ')
student4 = input('What is the name of the fourth student? ')

print('The presentation order will be... {}.'.format(random.sample([student1, student2, student3, student4], k=4)))
