#   File IO

my_file = open("welcome.txt", "wb")     # wb means write mood
print(my_file.mode)
print(my_file.name)
my_file.write(bytes("Hello everyone! welcome all to my youtube channel.", "UTF-8"))
my_file.close()