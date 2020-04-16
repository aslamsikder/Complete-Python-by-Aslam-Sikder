#   ডান পাশের স্ট্রিং-কে, বাম পাশে প্রিন্ট করার নিয়ম
print("%s Dhaka University of Engineering & technology."% ('DUET stands for'))
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

#   Print with new line
print("I have complete my B.Sc. Engineering from Southeast University and ")
print("now I am pursuing my M.Sc. Engg. at DUET.")

#   Remove new line
print("I have complete my B.Sc. Engineering from Southeast University and ", end="")
print("now I am pursuing my M.Sc. Engg. at DUET.")

#   Print same line multiple time
print("I love my Family.\n" * 5)
print("Good Morning Doctor!\n"*10)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

#   Basic Calculator
num1 = int(input())
num2 = int(input())

print("Addition Result: ", num1 + num2)
print("Subtraction Result: ", num1 - num2)
print("Multiplication Result: ", num1 * num2 )
print("Division Result: ", num1 / num2 )
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

#   Taking multiple variables in one line using split() and map() Function
num3, num4, num5 = map(int,input().split())

add_result = num3 + num4 + num5
print("Addition Result: %d" %add_result)             # For integer formatting, we use '%d' %variable_name
print("Subtraction Result: ", num3 - num4 - num5)