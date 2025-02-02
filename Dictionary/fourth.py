# methods in dictionary
# 1 . .keys() / returns all keys
name = {
    "first" : 90,
    "second" : 90.45,
    "first"  : "hello",
    "howaru" : "fine"
}

print(name.keys())

# 2. .values / returns values

print(name.values())

# .items / returns keys and values as tuple

print(name.items())
print(list(name.items())) #typecasting it into  l ist

# 2. .update

name.update({"fift" : "tonystark"})
print(name)

# adding multiple itmes to dicitonary

name.update({"sicht" : "hi" , "jupite" : 90})
print(name)