#   If Else statement

print("Enter your marks: ")
number = int(input())

if (number>=1 and number<=100):
    if (number<=100 and number>=80):
        grade = 'A+'
    elif (number<=80 or number>=70):
        grade = 'A'
    else:
        grade = 'less than 70% marks!'
    print("You got", grade)
else:
    print("You have entered an invalid marks!")