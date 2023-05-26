# Create a program that reads a value in meters and returns
# the converted value to centimeters and millimeters

size_in_meters = float(input('Type a number in meters to convert: '))

in_mm = size_in_meters * 1000
in_cm = size_in_meters * 100
in_dam = size_in_meters / 10
in_hm = size_in_meters / 100
in_km = size_in_meters / 1000

print('{}m represents {}mm, {}cm, {} dam, {}hm and {} km.'.format(size_in_meters, in_mm, in_cm, in_dam, in_hm, in_km))

