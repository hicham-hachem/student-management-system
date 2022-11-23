"""
This bloc is used to read the data from file and add them to the dictionary
And display the menu
"""
import all_cases


# This functiom is used to display the menu and ask for choice over and over
def return_function():
    print()
    print("MENU LIST")
    print("1 - Display Statistics")
    print("2 - Display All Students")
    print("3 - Add New Student")
    print("4 - Remove Student")
    print("5 - Enroll Existing Student in a Course")
    print("6 - Edit Student")
    print("7 - Display Student")
    print("8 - Exit")
    print()
    
    choice = input("Enter your choice:")
    all_cases.switch(choice)
    