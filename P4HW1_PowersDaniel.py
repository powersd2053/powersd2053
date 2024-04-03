#Daniel Powers
#03/27/24
#P4HW1
#Student Number and Letter Grades using loops

#Define Variabes
scores_list = []
scores = int(input("Enter how many scores you are evealating: "))
for num in range (scores):
    grade = float(input(f"Enter Score {num+1}: "))
    while grade < 0 or grade > 100:
        print("Score must be between 0 and 100")
        grade = float(input(f"Enter Score {num+1}: "))
    scores_list.append(grade)




lowest_grade = min(scores_list)
scores_list.remove(lowest_grade)

highest_grade = max(scores_list)
sum_ = sum(scores_list)
average = (sum_ / len(scores_list))


print()

print("------------Results------------")
(print)
#find lowest score
print (f"{'Lowest Score:':<20} {lowest_grade:.2f}")
#list scores
print (f"{'Modified List:':<20} {scores_list}")
#calculate  average
print (f"{'Average Score:':<20} {average:.2f}")


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

