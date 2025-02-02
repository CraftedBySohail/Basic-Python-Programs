# List is a mutable data type
# it is created using square bracket 
# we can insert elment in list as many as we want
# element are separated by commas
# it stores element of different data types

hello  = [1,2,2,3,4,5,4,3,2]
marks  = ["hello", 'g', 1,3,4,3,6.778]

print(hello,marks)

print(len(hello),len(marks))
print(type(hello),type(marks))

# accesing list element through index
for i in range(0,9):
    print(hello[i],end="")
print("\n")  
for i in range(0,7):
    print(marks[i],end="")

# modifying elements in list through index
marks[0] =  "SOHAIL"
print(marks)