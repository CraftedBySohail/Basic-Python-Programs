# Slicing in list
marks = [1,2,3,4,34,9.0,324]

print(marks[1:7])
print(marks) #original list remains the same

print(marks[:7]) #by default the indexing start from zero

print(marks[2:]) # ending index is len(marks)

print(marks[:])  #complete list will be printed

# negative index is also possible in list

print(marks[-7 : ])