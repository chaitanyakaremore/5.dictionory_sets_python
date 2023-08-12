myDict={
"barabar":"correct",
"baya":"right",
"udharkarastsa":"waytoward",

}
print("Options are ",myDict.keys())
a= input("Enter the hindi words\n")
# print("The meaning of your words is:",myDict[a])

#Below line will throw an error if the key is not present in the dictionary
print("The meaning of your word is :",myDict.get(a))