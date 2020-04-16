#   Creating an anonymous function

#   Sample Lambda Function
my_lambda = lambda x: 5*x + 1
print("The result is", my_lambda(3))

#   Lambda expression with multiple inputs

# Combine first name and last name into a single "Full Name"
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   aslam", "SiKDer"))

# Building quadratic finction
def build_Quadratic_function(a, b, c):
    # Return the function, f(x) = ax^2 + bx + c
    return lambda x: a*x**2 + b*x + c
f = build_Quadratic_function(2, 3, -5)
print(f(2))

#   We can write it in one line also
print(build_Quadratic_function(3, 0, 1)(2))     # 3x^2+1 is evaluated for x = 2



