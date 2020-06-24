# put your python code here
A = input()
B = input()
H = input()


def arithematic_func(first_number, second_number, operations):
    operations_list = ['+', '-', '/', '*', 'mod', 'pow', 'div']
    first_number = float(first_number)
    second_number = float(second_number)
    if second_number == 0.0 and (operations in ("mod", "/", "div")):
        return "Division by 0!"
    else:
        if operations in operations_list:
            if operations == 'mod':
                return first_number % second_number
            elif operations == 'pow':
                return first_number ** second_number
            elif operations == 'div':
                return first_number // second_number
            elif operations == '+':
                return first_number + second_number
            elif operations == '-':
                return first_number - second_number
            elif operations == '/':
                return first_number / second_number
            elif operations == '*':
                return first_number * second_number


print(arithematic_func(A, B, H))
