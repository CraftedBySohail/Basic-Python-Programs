# factorial of a number using recursion

def factorial(num):
    if(num == 1 or num == 0):
        return 1
    num = num * factorial(num-1)
    return num
number = int(input("Enter a number :"))
value = factorial(number)
print("The factoiral of a given number :",value)