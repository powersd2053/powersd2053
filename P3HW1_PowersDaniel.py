#Daniel Powers
#03/14/24
#P3HW1
#Student Number and Letter Grades

#Define Variabes
print("------Enter Student Grades-----")
num1 = float(input("Enter grade for Module 1: "))
num2 = float(input("Enter grade for Module 2: "))
num3 = float(input("Enter grade for Module 3: "))
num4 = float(input("Enter grade for Module 4: "))
num5 = float(input("Enter grade for Module 5: "))
num6 = float(input("Enter grade for Module 6: "))
grades = []
grades.append(num1)
grades.append(num2)
grades.append(num3)
grades.append(num4)
grades.append(num5)
grades.append(num6)
lowest_grade = min(grades)
highest_grade = max(grades)
sum_ = sum(grades)
average = (sum_ / len(grades))

print()

print("------------Results------------")
(print)
#find lowest score
print (f"{'Lowest Grade:':<20} {lowest_grade:.2f}")
#find highest score
print (f"{'Highest Grade:':<20} {highest_grade:.2f}")
#calculate sum
print (f"{'Sum of Grades:':<20} {sum_:.2f}")
#calculate  average
print (f"{'Average:':<20} {average:.2f}")
print("-------------------------------")
if average >= 90:
    print('Your grade is: A')
elif average > 80:
    print('Your grade is: B')
elif average > 70:
    print('Your grade is: C')
elif average > 60:
    print('Your grade is: D')

else:
    print('Your grade is: F')
