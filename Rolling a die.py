import random

while True:
    a=input("Enter(Y/n):").lower()[0];
    if(a=='y'):
            num1=random.randint(1,6)
            num2=random.randint(1,6)
            print("(",num1,",",num2,")")
    elif(a=='n'):
            print("Thanks for Playing!");
            break
    else:
            print("Invalid input!")
