"""
    Set is one kind of data types that doesn't return duplicate values.
    We can apply add(), update(), remove(), discard(), pop() etc functions
    in a Sets.
    To create Sets, we need to use Second Bracket { , }
"""

#   Creating Sets
s1 = {12, 3, 3, 3, 4, 5, 5, 5, 6, 15, 19, 19, 20, 20, 13, 21, 24, 25, 25, 28, 28}
print("The Elements of this sets are:", s1)

#   Operation on sets
#   Adding single value
s1.add(1995)

#   Adding multiple values
s1.update([123, 634, 423, 634, 432])
print("\nThe Modified Elements of this sets are:", s1)

print("\nThe length of the set is",len(s1))
print("The Minimum of the set is",min(s1))
print("The Maximum of the set is",max(s1))

#   If the element exist in the set, remove() will delete the element. If doesn't exist, it will through Error
s1.remove(1995)
#s1.remove(2020)
print("\nThe Modified Elements of this sets are:", s1)

#   If the element exist in the set, discard() will delete the element. If doesn't exist, it will not through Error
s1.discard(432)
s1.discard(2020)
print("\nThe Modified Elements of this sets are:", s1)

s2 = {1, 2, 3, 4, 6, 12}
s3 = {3, 6, 9, 12}
#   Intersection
print("\nThe result of intersection is:",s2.intersection(s3))

#   Union
print("The result of Union is:", s2.union(s3))

#   Difference
print("The result of difference is:", s2.difference(s3))

#   Disjoint
print("\nAre the two sets disjoint? -->", s2.isdisjoint(s3))

#   pop() return the element one by one
print(s2.pop())
print(s2.pop())
print(s2.pop())
print(s2.pop())
print(s2.pop())
print(s2.pop())