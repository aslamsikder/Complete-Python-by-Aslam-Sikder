"""
    Tuples is one kind of List that elements are not changeable.
    That means append(), insert(), update(), remove() etc functions
    are not applicable for the Tuples.
    To create tuples, we need to use First Bracket ()
"""
#   Creating Tuples
my_tuple1 = (1, 2, 3, 4, 5)
print("The values of the first Tuples are: ", my_tuple1)
print("The first three values of the Tuples: ", my_tuple1[0:3], '\n')

my_tuple2 = ('Aslam', 'Rakibul', 'Jowel', 'Razib', 'Shawon')
print("The values of the Second Tuples are: ", my_tuple2)
print("Print the 4th & 5th values of the tuples: ", my_tuple2[3:5])

# Operations that is not possible in Tuples
"""
my_tuple2.append('Iron Man')
'tuple' object has no attribute 'append'
"""
#   my_tuple2[2] = 'Rakibul Islam'
#   print(my_tuple2)

#   We can apply those operation by converting a Tuples into a List using Type casting
my_list = list(my_tuple2)
print("\nThe List is: ",my_list)

my_list.append('Iron Man')
my_list.insert(0, "Engineer")
print("The modified List is: ",my_list)

#   Converted the List into Tuples
my_tuple2 = tuple(my_list)
print("\nThis is the modified Tuples: ",my_tuple2)

#   Find the length, maximum &  minimum from the Lists
print("\nThe values of the first Tuples are: ", my_tuple1)
print("The Length of the First Tuples: ", len(my_tuple1))
print("The Minimum of the First Tuples: ", min(my_tuple1))
print("The Maximum of the First Tuples: ", max(my_tuple1))

