
# # Course Purchase Application
from colorama import Fore, Style, init
init(autoreset=True)
# Course catalog with course details with sample data        
course_catalog = {
    "Python Basics": {"price": 500, "duration": "4 weeks", "instructor": "John Doe"},
    "Data Science": {"price": 1000, "duration": "8 weeks", "instructor": "Jane Smith"},
    "Web Development": {"price": 750, "duration": "6 weeks", "instructor": "Alice Johnson"},
    "Machine Learning": {"price": 1200, "duration": "10 weeks", "instructor": "Bob Brown"}
}   
selected_courses = []  # List to store selected courses
print(Fore.GREEN + Style.BRIGHT + "Welcome to the Course Purchase Application!")
while True:
    course_name = input("Enter the course name you want to know about (or type 'exit' to finish): ").strip()
    if course_name.upper() == "EXIT":
        break
    elif course_name in course_catalog:
        selected_courses.append(course_name)
        # details = course_catalog[course_name]
        # print(f"Course Name: {course_name}")
        # print(f"Price: ${details['price']}")
        # print(f"Duration: {details['duration']}")
        # print(f"Instructor: {details['instructor']}")
        # total_price = sum(course_catalog[course]['price'] for course in selected_courses)
        # print(f"Total price for selected courses: ${total_price}")
        print(f"You have selected course {course_name} the following courses successfully!")
    else:
        print("Course not found. Please enter a valid course name.")
        print("Be patient we are adding more courses soon!")

for idx, course in enumerate(selected_courses, start=1):
    details = course_catalog[course]
    print(f"{idx}. {course} - Instructor: {details['instructor']}, Duration: {details['duration']}, Price: ${details['price']}")    
total_amount = sum(course_catalog[course]['price'] for course in selected_courses)
print(f"\nTotal amount for selected courses: ${total_amount}")  


# * Copilot suggested code with dictionary inside dictionary *
# # Course catalog with dictionary inside dictionary
# course_catalog = {
#     "Python Basics": {"price": 500, "duration": "4 weeks", "instructor": "John Doe"},
#     "Data Science": {"price": 1000, "duration": "8 weeks", "instructor": "Jane Smith"},
#     "Web Development": {"price": 750, "duration": "6 weeks", "instructor": "Alice Johnson"},
#     "Machine Learning": {"price": 1200, "duration": "10 weeks", "instructor": "Bob Brown"}
# }
# selected_course = {}
# # Function to display course details
# def display_course_details(course_name):
#     if course_name in course_catalog:
#         selected_course.append(course_name)
#         details = course_catalog[course_name]
#         print(f"Course Name: {course_name}")
#         print(f"Price: ${details['price']}")
#         print(f"Duration: {details['duration']}")
#         print(f"Instructor: {details['instructor']}")
#         #you have selected the courses successfully and total price for all selected courses
#         print(f"Total price for selected courses: ${sum(course_catalog[course]['price'] for course in selected_course)}")

#         print("you have selected the following course successfully!")
#     elif course_name == "EXIT":
#         break
#         print("Please enter a valid course name.")   
#     else:       
#         print("Course not found.")

# # Main application
# def main():
#     print("Welcome to the Course Purchase Application!")
#     course_name = input(f"Enter the course {course_name} name you want to know about: ").strip().upper()
#     display_course_details(course_name)

# if __name__ == "__main__":
#     main()

