from datetime import date

# Create an algorithm that receive a year and returns if it's a leap year or not.

year = int(input('Tell me a year to analyze (YYYY) or inform 0 to analyze the current year: '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The year {} is a leap year!'.format(year))
else:
    print('The year {} is not a leap year!'.format(year))
