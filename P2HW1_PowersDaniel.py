#Daniel Powers
#02/28/24
#P2HW1
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

#Variable and print statements

print('This program calculates and displays travel expenses')
print()
budget =float(input('Enter Budget: '))
print()
destination =str(input('Enter your travel destination: '))
print()
gas =float(input('How much do you think you will spend on gas? '))
print()
hotel =float(input('Approximately, how much will you need for acomodation/hotel?: '))
print()
food =float(input('Last, how much do you need for food?: '))
print()
expenses =(gas + hotel + food)
balance =float(budget - expenses)
print()
print('------------Travel Expenses------------')
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel:':<20} ${gas:.2f}")
print(f"{'Accommodation:':<20} ${hotel:.2f}")
print(f"{'Food:':<20} ${food:.2f}")
print('--------------------------------------')
print()
print(f"{'Remaining Balance:':<20} ${balance:.2f}")
