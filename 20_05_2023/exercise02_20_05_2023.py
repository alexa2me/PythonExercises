# Create a program that reads an input and return the primitive type and several
# other information with is...

some_input = input('Type something: ')

print('The type of you input is ', type(some_input))
print('Is your input a number or is it possible to convert to it? ', some_input.isnumeric())
print('Is your input alphabetic or is it possible to convert to it? ', some_input.isalpha())
print('Is your input alphanumeric or is it possible to convert to it? ', some_input.isalnum())
print('Is your input all uppercase? ', some_input.isupper())
print('Is your input all lowercase? ', some_input.islower())
print('Does your input have only spaces? ', some_input.isspace())
print('Is your input a decimal number? ', some_input.isdecimal())
print('Is your input a reserved identifier in Python? ', some_input.isidentifier())
print('Does your input have digits and at least one character? ', some_input.isdigit())
print('Is your input capitalized? ', some_input.istitle())
