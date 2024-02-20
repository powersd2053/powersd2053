#Daniel Powers
#02/14/24
#P1HW1
#Basic output with variables (Exercise 2)


#Pseudocode

#Get Budget
#Get Destination
#Get gas
#Get hotel
#Get food
#Add expenses
#Deduct expenses from budget
#Display results

#Define variables
print('This program calculates and displays travel expenses')
print()
budget =int(input('Enter Budget: '))
print()
destination =str(input('Enter your travel destination: '))
print()
gas =int(input('How much do you think you will spend on gas? '))
print()
hotel =int(input('Approximately, how much will you need for acomodation/hotel?: '))
print()
food =int(input('Last, how much do you need for food?: '))
print()
expenses =(gas + hotel + food)
balance =int(budget - expenses)
print()
print('------------Travel Expenses------------')
print('Location:', destination)
print('Initial Budget:', budget)
print()
print('Fuel:', gas)
print('Accommodation:', hotel)
print('Food:', food)
print()
print('Remaining Balance:', balance)
