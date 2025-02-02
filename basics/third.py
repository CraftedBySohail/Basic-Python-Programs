# Taking input and type casting 

# Taking input from and user and displaying it

hello = input("Enter your name :")
print("You entered :",hello)

Rollno = input("Enter your Roll no")
print("You entered :",Rollno)
print(type(Rollno))
# for roll no the type is showing string eventough it is not
# to solve this we do typecasting

Rollno2 = int(input("Enter your Roll no"))
print("You entered :",Rollno2)
print(type(Rollno2))