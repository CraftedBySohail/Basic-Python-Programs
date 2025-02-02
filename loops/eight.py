# Program to find factorial of first n numbers using for loops
lenth = int(input("Enter a number :"))
sum = 1
for i in range(lenth,0,-1):
    sum = sum * i
print("The factoial is :",sum)