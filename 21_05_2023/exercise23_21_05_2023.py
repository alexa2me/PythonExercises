# Create an algorithm that reads the name of a city and returns if the city name
# starts with the word "Santo"

city_name = input('What is the name of your city? ')

city_upper = city_name.upper()

print('Does the city name starts with the word SANTO? {}'.format('SANTO' in city_upper[0:5]))
