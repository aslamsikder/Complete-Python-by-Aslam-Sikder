#   Loops

print("How many times you want to execute your loop:")
num = int(input())
for i in range(0,num):
    print(i)

#   Using loops in lists
book_list = ['Bangla', 'English', 'Math', 'Physics', 'chemistry', 'Biology']
for book in book_list:
    print(book)
print('\n')

#   Nested Loop in Nested Lists
nes_list = [[1, 2, 3], ['Aslam', 'Rakibul'], [24.5, 25]]
for item in nes_list:
    for i in item:
        print("Item is ", i)