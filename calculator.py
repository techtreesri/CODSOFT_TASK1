print("~CALCULATOR~")

num1=float(input("enter first number here:"))
num2=float(input("enter second number here:"))

print("press 1 for Addition \n press 2 for Subtraction \n press 3 for Multiplication \n press 4 for Division1")

choice=int(input("entr your choice from 1 to 4:"))

if(choice == 1 ):
    print("The addition of given two numbers is=",num1 + num2)

elif(choice == 2):
    print("The subtraction of given two numbers is=",num1 - num2)

elif(choice == 3):
    print("The multiplication of given two numbers is=",num1 * num2)

elif(choice == 4):
    print("The division of given two numbers is=",num1 / num2)

else:
    print("Invalid Input")