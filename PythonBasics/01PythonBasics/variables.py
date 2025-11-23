#scalar variable
#string variable
from datetime import datetime


name = 'pavan'
#interger variable
age = 25
#float variable
height = 5.9
#boolean vaiable


is_student = False

#Display the vaiables
print("Name: ",name, "is type of: ", type(name))
print('Age:', age, "is type of: ",type(age))
print('Adult:', is_student, "is type of: ", type(is_student))

# Type conversion
age_str = "56"
print('Age as string:', age_str, type(age_str))
print('after convestion age type')
age_int  = int(age_str)
print('age as integer', age_int, type(age_int))
#input  
new_age = input("Enter your age: ")
# if condition
if int(new_age) > 18:
    print("You are eligible to vote")
    print(f"{name} with hieght {height} is an adult{datetime.now()}")
elif int(new_age) == 18:
    print("Just eligible to vote")
else:
    print("Not eligible to vote")