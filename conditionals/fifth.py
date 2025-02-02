# Take 3 positive integer as input and print the greatest them all using nested if else
number1 = int(input("Enter 1st number :"))
number2 = int(input("Enter 2nd number :"))
number3 = int(input("Enter 3rd number :"))


if number2 == number3 == number1 :
    print("The number are equal") 
elif number1 > number2 :
    if number1 > number3:
        print("The greatest number is :",number1)
    else : 
        print("The greatest number is :",number3)
else :
    if number2 > number3 :
       print("The greatest number is :",number2)
    else :
        print("The greatest number is :",number3)