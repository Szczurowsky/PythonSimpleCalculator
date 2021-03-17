import logging


class Calculator:

    def __call__(self):
        numbers = []
        __i = int(0)
        input_numbers = 2  # Soons
        while input_numbers != __i:
            last_number = input("Type number " + str(__i+1) + "\n")
            try:
                last_number = float(last_number)
            except Exception as e:
                logging.info(e)
                print('This is not number :/\n')
                Calculator.__call__(self)
            numbers.append(last_number)
            del last_number
            __i = __i + 1
        return Calculator.do(self, numbers)

    def do(self, numbers, operation=1):
        try:
            operation = input("What u want to do: \n 1 - add "
                              "\n 2 - subtract \n 3 - multiply \n 4 - division \n")
            operation = int(operation)
        except Exception as e:
            logging.info(e)
            print('Type number 1 to 4 to select')
        if operation == 1 or operation == 2 or operation == 3 or operation == 4:
            i = int(0)
            while i != len(numbers):
                __temp = int(numbers[i])
                numbers[i] = __temp
                i = i + 1
            if operation is 1:
                return numbers[0] + numbers[1]
            if operation is 2:
                return numbers[0] - numbers[1]
            if operation is 3:
                return numbers[0] * numbers[1]
            if operation is 4:
                return numbers[0] / numbers[1]
        else:
            print('Type number 1 to 4 to select')
            Calculator.do(self, numbers)


new_calc = Calculator()
print('Result is', new_calc())
