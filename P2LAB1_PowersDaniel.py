#Daniel Powers
#03/04/24
#P2LAB1
#Driving Costs (Variables and Expressions)

#Define Variables

mpg = float(input("Enter your MPG: "))
gas_price = float(input("Enter the price of gas: "))
distance1 = 20
distance2 = 75
distance3 = 500
cost1 = float(distance1 / mpg * gas_price)
cost2 = float(distance2 / mpg * gas_price)
cost3 = float(distance3 / mpg * gas_price)

#Print Statements

print(f"Cost to drive 20 miles is ${cost1:.2f}")
print(f"Cost to drive 75 miles is ${cost2:.2f}")
print(f"Cost to drive 500 miles is ${cost3:.2f}")

