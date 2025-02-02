# . Dictionaries indeed lack the concept of indexing because they are unordered collections.
dictionaries =  {
    "Book1" : "hellp",
    "book1" : 67,
    78   : "hello"
 }

print(dictionaries)
print(type(dictionaries))


# overwritng dictionary using key

dictionaries["Book1"] = 98;
print(dictionaries)

# null dictionaries
dictory = {
    
}
print(dictory)