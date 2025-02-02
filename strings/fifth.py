
hello = "hello world"

# 1. capitalize 1st char
print(hello.capitalize())
# only capitalise this string and not the original one
print(hello)

# 2. Replace all occurence of old value
print(hello.replace("h","s"))
# we can replace substring too
print(hello.replace("sello","hello"))


#3. find function returns index of that char
print(hello.find("o"))
# we can search the word too
print(hello.find("world"))

# if no word is present in string it returns negative integer
print(hello.find("solo")) 

# 4 . count  the no of substring
print(hello.count("l"))