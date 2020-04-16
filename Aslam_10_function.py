"""
    There are two types of function. They are as follows
    1. Built in Function & 2. User define Functions.
    We start writing function using def keyword.
"""

def sum(n):
    #    Function with parameter
    result = n*(n+1)/2
    return  result  # Return the function value
print("Summation is: ", sum(100))


def average():
    #   Function without parameter
    print("Enter three numbers: ")
    #   Taking input from User
    num1, num2, num3 = map(int, input().split(','))
    #num1 = int(input())
    #num2 = int(input())

    result = (num1+num2+num3)/3  # Calculate Average
    return result   # Return the value
print("Average of this two numbers: %.2f" %average())   #For float formatting, we use '%.2f' %variable_name

"""
    For string formatting, we use '%s' %variable_name
    For float formatting, we use '%.2f' %variable_name
    For integer formatting, we use '%d' %variable_name
"""