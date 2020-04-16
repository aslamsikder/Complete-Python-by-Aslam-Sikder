#   Reading the content of a file

open_file = open("MySocialProfilesLinks.txt", "r+")     #  r+ is used to read & write the file
read_text = open_file.read()
print(read_text)
open_file.close()