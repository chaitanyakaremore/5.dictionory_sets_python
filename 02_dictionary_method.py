myDict ={
    "Fast":"In a Quick Manner",
    "Chaitanya":"A Coder",
    "Marks":[1,2,5],
    "anotherdict":{'Chaitanya':'Player'}
}

#dictionary Methods
print(list(myDict.keys())) #prints the keys of the dictionary
print(myDict.values()) #prints the values of the dictionary
print(myDict.items()) #prints the (keys,values) for all contents of the dictionary
print(myDict)
updateDict = {
    "Lovish":"Friend",
     "Divya":"Friend",
      "shubham":"Friend",
     "Chaitanya":"A Dancer",
}
myDict.update(updateDict) #updates the dictionary by adding key-value pairs from updatDict
print(myDict)

print(myDict.get("Chaitanya")) #print value associated with key "Chaitanya"
print(myDict["Chaitanya"]) #print value associated with key "Chaitanya"

#The difference between .get and []
print(myDict.get("Chaitanya2")) #Return None as harry2 is not present in dictionary
print(myDict("Chaitanya2")) #throw the error as harry2 is not present in the dictionary