#   While loops

print("Enter a number")
num = int(input())

while(num>4):
    print("Number is greater than 4")
    num = int(input())
    if (num == 10):
        break
    if (num == 9):
        continue
    print("Loop ended")