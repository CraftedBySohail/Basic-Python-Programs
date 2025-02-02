# Match case
# Making calculator

num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))

operator = str(input("ENter operator :"))

match operator :
    case "+" :
        print("The result is :",num1 + num2)
    case "-" :
        print("The result is :",num1 - num2)
    case "*" :
        print("The result is :",num1 * num2)
    case "/" :
        print("The result is :",num1 / num2)    
    case "**":
        print("The result is :",num1 ** num2)  
    case _ :
        print("PLease enter a valid operator")