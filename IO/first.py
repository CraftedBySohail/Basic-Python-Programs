f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))

# reading l ine by line
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)
# always close file once created
f.close()