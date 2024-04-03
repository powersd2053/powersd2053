#Daniel Powers
#3/27/24
#P4LAB2
#Use a while loop

#Get two integer values from user
var1 = int(input("Enter the smaller integer: "))
var2 = int(input("Enter the larger integer: "))

#while var1 is larger, allow user to re-enter the vaules

while var1 >= var2:
    print("First number must be smaller. Try again")
    var1 = int(input("Enter the smaller integer: "))
    var2 = int(input("Enter the larger integer: "))

#The while looop has broken because use entered values correctly

for num in range(var1, var2+1, 5):
    print(num, end = " ")#after comma will prevent output from entering new line
