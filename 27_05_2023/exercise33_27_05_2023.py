# Create an algorithm that receives a salary and returns the new value with a raise.
# If the salary is greater than R$1,250 the raise will be of 10% and if less so the raise will be of 15%

salary = float(input('What is your salary: '))

if salary > 1250:
    new_salary = salary+(salary*(10/100))
    print('The new salary with a raise of 10% will be R${:.2f}'.format(new_salary))
else:
    new_salary = salary+(salary*(15/100))
    print('The new salary with a raise of 15% will be R${:.2f}'.format(new_salary))
