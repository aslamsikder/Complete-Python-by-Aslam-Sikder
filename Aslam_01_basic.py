'''This is Multiline comment'''
"""
Aslam Sikder
Software Engineer
"""

#   Using Print Function
print("Hello world!") # I am showing hello world in the screen.
print("- - - - - - - - - - - - - - - - - - - - - - -")

#   Vsriable Declaratin
str1 = "Aslam Sikder" #  This is a string
print("This is ",type(str1))

age = 24    # This is an Integer
print("This is ",type(age))

age2 = "6"

weight = 65.5 # This is a float
print("This is ",type(weight))

#   Type Casting
age2 = int(age2)
result = age + age2
print(result)
print(type(result))

result = str(result)    #   Converted into String
print(result)
print(type(result))

#   String Concate
str3 = "\nAslam Sikder's age is "
age3 = 25
age3 = str(age3)
print(str3 + age3)
print("- - - - - - - - - - - - - - - - - - - - - - -")

'''Main data types of python are
    Numbers, Strings, Lists, Tuples & Dictionaries    
'''
#   Arithmatic Operation
print("The addition of 2 + 10 = ", 3+10)            #   Addition
print("The subtraction of 2 - 10 = ", 3 - 10)       #   Substraction
print("The Multiplication of -3 * -7 = ", -3 * -7)  #   Multiplication
print("The Division of -28 / -7 = ",-28 / -7)       #   Division
print("The Division of 5 ** 3 = ", 5 ** 3)          #   Exponential
print("The Division of 3 // 5 = ", 3 // 5)          #   Float Division
print("- - - - - - - - - - - - - - - - - - - - - - -")

#    Multi Line string
msl = '''I am Aslam Sikder. I live in Gazipur City. I am a Software Engineer.
I have completed B.Sc. in Computer Science & Engineering from Southeast University, Bangladesh. 
My obtained CGPA is 3.75/4.00. And currently, I am pursuing M.Sc. Engg. at Dhaka University of 
Engineering & Technology (DUET).'''
print(msl)
print("- - - - - - - - - - - - - - - - - - - - - - -")

