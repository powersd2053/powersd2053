#Daniel Powers
#4/21/24
#P5HW
#User-defined functions

#Menu Options
def mainMenu():
    while True:
        print()
        print ("Welcome to Math Quiz")
        print()
        print("MAIN MENU")
        print("------------------------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print()


#Get input from user
        num = input("Please enter a menu option: ")
        if num == "1":
            displayAddition()
        elif num == "2":
            displaySubtraction()
        elif num == "3":
            print("Thank you for playing... Bye!")
            exit()
        else:
            num = input("Error! Please hit any key to return to main menu: ")

#Define functions
#Addition

def displayAddition():
        attempts = 1
        print()
        print("Add these numbers: ")
        import random

        num1 = random.randint(1, 100)
        print(num1)
        num2 = random.randint(1, 100)
        print(num2)
        print("----")
        num3 = num1 + num2
        num4 = int(input("Enter your answer: "))
        
        while num4 != num3:
            if num4 < num3:
                print("Your answer is too low! Try again. ")
                num4 = int(input("Enter your answer: "))
                attempts +=1
            elif num4 > num3:
                print("Your answer is too high! Try again. ")
                num4 = int(input("Enter your answer: "))
                attempts +=1
                        
        print("GREAT JOB!")
        print("Number of attempts:", attempts)
        print()

#Subtraction
def displaySubtraction():
        attempts = 1
        print()
        print("Subtract these numbers: ")
        import random
        num1 = random.randint(1, 100)
        print(num1)
        num2 = random.randint(1, 100)
        print(num2)
        print("----")
        num3 = num1 - num2
        num4 = int(input("Enter your answer: "))

        while num4 != num3:
            if num4 < num3:
                print("Your answer is too low! Try again. ")
                num4 = int(input("Enter your answer: "))
                attempts +=1
            elif num4 > num3:
                print("Your answer is too high! Try again. ")
                num4 = int(input("Enter your answer: "))
                attempts +=1
                        
        print("GREAT JOB!")
        print("Number of attempts:", attempts)
        print()

mainMenu()

