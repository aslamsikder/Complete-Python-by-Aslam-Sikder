#   String operations

string1 = "Hello everyone! What's going on?"
string2 = " this is Aslam Sikder from Gazipur."

print(string1[0:3])     # Print from the first Index
print(string2[-8:])     # Print from the last Index
print(string1[:-2])     # Print without last two Index
print(string2[8:-14])   # Print without first & last Index

print(string2.capitalize())         # For capitalizing the first letter of a sentence.
print("It has started form: ",string2.find("Sikder"))       # To find out a set of character
print("If the string doesn\'t exist, it will return: ", string2.find("Dhaka"))      # -1 means string doesn't exist
print(string2.replace("Gazipur", "Dhaka"))      # It will replace all the string what is started with "Gazipur"

#   concatenation
new_string = string1 + string2      # Adding two Strings
print('%s' %new_string)             # For string formatting, we use '%s' %variable_name