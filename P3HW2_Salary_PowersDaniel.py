#Daniel Powers
#3/18/24
#P3HW2
#Salary with Overtime


#Define variables

employee = str(input("Enter employee's name: "))
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked <=40:
    overtime_hours = 0
    regular_hours = hours_worked
else:
    overtime_hours = float(hours_worked - 40)
    regular_hours = 40
    
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours *(pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay
    

#Print statements

print("-----------------------------------------------------------------------------------------")
print("Employee name: ", employee)
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("-----------------------------------------------------------------------------------------")

print(f"{hours_worked:<15.2f}${pay_rate:<15.2f}{overtime_hours:<15.2f}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}")



