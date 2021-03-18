from calculator import EndCalculator

new_calc = EndCalculator()
print('Result is', new_calc())
action = input('Enter to end, - to use again\n')
while action == '-':
    print('Result is', new_calc())
    action = input('Enter to end, - to use again\n')
