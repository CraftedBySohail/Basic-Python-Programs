f = open("demo1.txt","r")
data = f.read()
print(data)
# once a data is read completelt the pint er will be pointing to the end

data = f.readline()