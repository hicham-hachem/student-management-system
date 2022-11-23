"""
Implement Python Switch Case Statement using Dictionary
instead of using if conditions
The basic structure of this code was inspired from this page
https://flexiple.com/python/python-switch-case
"""
import functions
import menu

# Defining a function for every case
# This case function will call another function from functions page that will do the job

# Except the exit function
    # Every function at the end will demand a new choice number
    # every function will call again the switch function with our new choice as parameter

# 1
def display_statistics():
    functions.display_statistics_func()
    menu.return_function()

# 2
def display_all_students():
    functions.display_all_students_func()
    menu.return_function()

# 3
def add_new_student():
    functions.add_new_student_func()
    menu.return_function()

# 4
def remove_student():
    functions.remove_student_func()
    menu.return_function()

# 5
def enroll_existing_student_in_a_course():
    functions.enroll_existing_student_in_a_course_func()
    menu.return_function()

# 6
def edit_student():
    functions.edit_student_func()
    menu.return_function()

# 7
def display_student():
    functions.display_student_func()
    menu.return_function()

# 8
def exit():
    functions.exit_func()

# This function is used if the user enter a value not from 1 to 8
def default():
    print("Incorrect input")
    menu.return_function()

##############################################################################

# Creating a switcher dictionary
switcher = {
    "1": display_statistics,
    "2": display_all_students,
    "3": add_new_student,
    "4": remove_student,
    "5": enroll_existing_student_in_a_course,
    "6": edit_student,
    "7": display_student,
    "8": exit
    }

##############################################################################

# defining the switch function
def switch(choice):
    return switcher.get(choice, default)()