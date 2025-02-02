# Take 3 positive integer as input and print the greatest them all

number1 = int(input("Enter 1st number :"))
number2 = int(input("Enter 2nd number :"))
number3 = int(input("Enter 3rd number :"))

if number1 > number2 and number1 > number3 :
    print("The greatest number is :",number1)
elif  number1 < number2 and number2 > number3:
    print("The greatest number is :",number2)
else :
    print("the greatest number is :",number3)