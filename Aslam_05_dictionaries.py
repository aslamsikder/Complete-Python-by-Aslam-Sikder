"""
    Dictionary is one kind of data types that have two elements
    separated by ':'colon. First one is 'Value' & Second is the 'key'.
    To create Dictionary, we need to use Second Bracket & Colon [ : ]
"""
#   Creating a Dictionary
names = {'Aslam' : 25,
         'Tanjina': 15,
         'Zakia': 2.5,
         'Rakibul': 24}
print("My dictionaty consists of: ", names)

#   Accessing from Dictionary
print("\nThe keys of the dictionary are: ", names.keys())
print("The values of the dictionary are: ", names.values(), '\n')

#    Showing Specific Key's value
print("The age of Aslam is", names['Aslam'])
print("The age of Zakia is",names['Zakia'])