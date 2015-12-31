'''
Finding the largest/smallest value if the value is unknown

'''

largest = None
smallest = None
while True:
        user_input = input('Enter a number: ')
        if user_input == 'done':
            print('Maximum is',largest)
            print('Minimum is',smallest)
            break
        try:
                var = int(user_input)
        except:
                print('Invalid input')
                continue
        for value in user_input:
                if smallest is None:
                        smallest = value
                elif value < smallest:
                        smallest = value
        for value2 in user_input:
                if largest is None:
                        largest = value2
                elif value2 > largest:
                        largest = value

'''
TODO: Make negative numbers visible
'''
