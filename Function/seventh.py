# calculate the sum of n natural number using recursion
def natural_number(num):
    if (num == 0):
        return 0
    else:
        return num + natural_number(num-1)

number = int(input("Enter a number :"))

value = natural_number(number)
print("the sum of the n natural number is :",value)