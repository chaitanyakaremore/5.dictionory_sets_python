#An empty set can be created using the below Syntex:
b = set()
print(type(b))


#Addind values to empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) #adding value repeatedly does not change a set
b.add((4,5,6))

print(b)

#Accessing Elements
# b.add({4:5}) #Cannot add list or dictionary to set

print(len(b)) #print the length of sets

#Removing of an item
b.remove(5) #Removes 5 front set b
# b.remove(15) #throw  an error while trying to remove 15(which is not present in  the set)
print(b)

print(b.pop())