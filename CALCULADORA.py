def welcome():
    print('''
Welcome to Calculator
''')
...
# Don’t forget to call the function
welcome()

def calculate():
    operation = input('''
please type in the math operation you would like complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter your first number'))
    number_2 = int(input('Please enter your second number'))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, Please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    if calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()
calculate()
