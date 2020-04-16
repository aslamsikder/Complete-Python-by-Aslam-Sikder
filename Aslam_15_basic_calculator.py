#   Building a calculator using class

class Calculator:
    """
        Perform addition, subtraction, multiplication & Division
    """

    def addition(self, num1, num2):
        return num1 + num2
    # 'self' works like 'this' keyword of other language

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "It is impossible to divide by zero!"

    def square(self, num1, num2):
        return num1 ** num2

my_calculator = Calculator()        # created an object of Calculator() class

add_result = my_calculator.addition(105, 15)        # We use dot symbol (.) after the object to access the method.
print(add_result)

sub_result = my_calculator.subtraction(105, 15)
print(sub_result)

mult_result = my_calculator.multiplication(15, 8)
print(mult_result)

div_result = my_calculator.division(105, 15)
print(div_result)

div_result = my_calculator.division(105, 0)
print(div_result)

sq_result = my_calculator.square(5,4)
print(sub_result)



