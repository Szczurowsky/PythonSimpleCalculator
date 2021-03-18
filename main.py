import logging


class Calculator:

    def do(self, given_numbers, *operations):
        if len(operations) == 0:
            try:
                operation = input("What u want to do: \n 1 - add "
                                  "\n 2 - subtract \n 3 - multiply \n 4 - division \n")
                operation = int(operation)
            except Exception as e:
                logging.info(e)
                print('Type number 1 to 4 to select')
                return Calculator.do(self, given_numbers)
        if len(operations):
            operation = operations[0]
        else:
            operation = 0
        if operation == 1 or operation == 2 or operation == 3 or operation == 4:
            i = int(0)
            __temp = float(0)
            while i != len(given_numbers):
                if type(__temp) is int:
                    __temp = int(given_numbers[i])
                else:
                    __temp = float(given_numbers[i])
                given_numbers[i] = __temp
                i = i + 1
            if operation is 1:
                return given_numbers[0] + given_numbers[1]
            if operation is 2:
                return given_numbers[0] - given_numbers[1]
            if operation is 3:
                return given_numbers[0] * given_numbers[1]
            if operation is 4:
                return given_numbers[0] / given_numbers[1]
        else:
            print('Type number 1 to 4 to select')
            return Calculator.do(self, given_numbers)


class EndCalculator(Calculator):
    def __call__(self):
        numbers = []
        __i = int(0)
        input_numbers = 2  # Soon
        while input_numbers != __i:
            last_number = input("Type number " + str(__i + 1) + "\n")
            try:
                last_number = float(last_number)
            except Exception as e:
                logging.info(e)
                print('This is not number :/\n')
                return Calculator.__call__(self)
            numbers.append(last_number)
            del last_number
            __i = __i + 1
        return Calculator.do(self, numbers)


#new_calc = EndCalculator()
#print('Result is', new_calc())
#action = input('Enter to end, - to use again\n')
#while action == '-':
 #   print('Result is', new_calc())
 #   action = input('Enter to end, - to use again\n')
