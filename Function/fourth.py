# print the factorial
def factorial(num):
    sum = 1
    for i in range(1,num+1,1):
        sum = sum*i
    return print("the factorial is :",sum)
number = int(input("Enter a number :"))
factorial(number)