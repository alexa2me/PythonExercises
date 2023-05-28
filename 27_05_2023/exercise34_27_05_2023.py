# Create an algorithm that receives 3 lengths of straight lines and returns if it's possible to create a triangle.

length1 = float(input('First length: '))
length2 = float(input('Second length: '))
length3 = float(input('Third length: '))

check_length1 = abs(length2-length3) < length1 < length2+length3
check_length2 = abs(length1-length3) < length2 < length1+length3
check_length3 = abs(length1-length2) < length3 < length1+length2

if check_length1 and check_length2 and check_length3:
    print('The lengths are {}, {} and {} and they can create a triangle =).'.format(length1, length2, length3))
else:
    print('The lengths are {}, {} and {} and they can not create a triangle =(.'.format(length1, length2, length3))
