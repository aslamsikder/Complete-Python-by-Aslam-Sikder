"""
    List is one kind of data types that elements are changeable.
    We can apply append(), insert(), update(), remove() etc functions
    in a Lists.
    To create Lists, we need to use Third Bracket []
"""
#   Creating List
university = ['SEU', 'DUET', 'BUET']

#   Print the Lists
print("My Lists = ", university)

#   Accessing Lists Element
#   Index of a list starts from 0, 1, 2, 3, . . . n
print("The 2nd value of the Lists = ", university[2], '\n')

#   Update Lists Elements
university[2] = "CUET"
print("This is my new Lists = ", university)

# Print Lists Elements within a specific range
print("Print the List's value from 0 to 1 : ", university[0:2])


#   Operation on List

book_list = ['Bangla', 'English', 'Math', 'Physics', 'chemistry', 'Biology']
print("Book List for Class Nine (Science): ", book_list)

#   Adding new Element
book_list.append('Sociology')
print("1. Modified Book list for Class Nine (Science):", book_list)

#   Adding new Element in a specific Index
book_list.insert(3,'Higher Math')
print("2. Modified Book list for Class Nine (Science):", book_list)

book_list.insert(4,'Humanity')
print("3. Modified Book list for Class Nine (Science):", book_list)

# Remove an Element from the Lists
book_list.remove('Humanity')
print("4. Modified Book List for class nine (Science):", book_list)

#   Temporarily add Element to the List using plus '+' sign
print("5. Modified Book List for class Nine (Science):", book_list + ['ICT', 'Islamic Studies', 'Bangladesh & World'], '\n')

#   Find the length, maximum &  minimum from the Lists
print("The book List for class nine (Science):", book_list)

print("The Length of the Lists: ", len(book_list))
print("The Maximum of the list: ", max(book_list))
print("The Minimum of the List: ", min(book_list))


