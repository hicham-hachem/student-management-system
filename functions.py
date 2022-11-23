"""
This page contains all the functions
"""
import sys # needed to exit the running task
import matplotlib.pyplot as plt #import visuallizing library matplot.lib
import read_data as rd

#####################################################################
# 1
# This function display some statistics
def display_statistics_func():
    students_count = 0
    students_fsw = 0
    students_fcs = 0
    fsw_22 = 0
    # Looping through outer_dict to count the students
    for key, value in rd.outer_dict.items(): # O(n)
        students_count += 1

        # Checking if the students are enrolled in FSW
        if (value["course_id"])[0:3]=="FSW":
            students_fsw += 1
            # Checking the year of the students that are enrolled in FSW
        if (value["course_id"])[0:5]=="FSW22":
            fsw_22 += 1
        # Checking if the students are enrolled in FCS
        if (value["course_id"])[0:3]=="FCS":
            students_fcs += 1

    print()
    print("Total Number of FCS Students:", students_fcs)
    print("Total Number of FSW Students:", students_fsw)
    print("Students enrolled in FSW 2022", fsw_22)
    print()

    # creating the dataset
    data = {"students_fcs": students_fcs, "students_fsw": students_fsw, "fsw_22": fsw_22}
    k = list(data.keys())
    v = list(data.values())

    fig = plt.figure(figsize = (5, 2.5))
 
    # creating the bar plot
    plt.bar(k, v, color ='maroon', width = 0.4)
    
    plt.xlabel('Token course')
    plt.ylabel('No. of students')
    plt.title('Students statistics')
    plt.show()

#####################################################################
# 2
outer_list = []
# This function is used to get the data from the dictionary
def choose_function(key, value):
    # Creating a list of three None items
    inner_list = [None]*3
    inner_list[0] = key[5:7]
    inner_list[1] = value.get("first_name")
    inner_list[2] = value.get("last_name")
    # Add the inner_list to the outer_list
    outer_list.append(inner_list)

# This function is used to sort a list
def sort_list_function(outer_list):
    # Bubble sort algorithme (This algorithme was used in class)
    # Loop through elements from 0 to n
    for i in range(0,len(outer_list)): # O(n^2)
        #Fix the last i elements in place and loop through the remaining elements (j: 1 -> n-i)
        for j in range(1,len(outer_list)-i): # O(n)
            # Comparing the last_name in every list
            # If first>second
            if outer_list[j-1][2] > outer_list[j][2]:
                # Swap elements position
                outer_list[j-1], outer_list[j] = outer_list[j], outer_list[j-1]
    # Looping through the sorted list to print it
    for i in range(0,len(outer_list)):   # O(n)  
        print("Applied year: 20" + outer_list[i][0] + "  First name: " + outer_list[i][1] + "  Last name: " + outer_list[i][2])
        
# This function is used to display a list of all or specific students
def display_all_students_func():
    print()
    print("What do you want to list?")
    print("1 - All the students")
    print("2 - The students enrolled in FCS only")
    print("3 - The students enrolled in FSW only")
    print()
    choice2 = input("Enter your choice:")
    print()

    # Checking the input choice of the user
    if choice2=="1":
        for key, value in rd.outer_dict.items(): # O(n)
            choose_function(key, value)
        sort_list_function(outer_list)
        outer_list.clear()

    elif choice2=="2":
        for key, value in rd.outer_dict.items(): # O(n)
            if value.get("course_id")[0:3]=="FCS":
                choose_function(key, value)
        sort_list_function(outer_list)
        outer_list.clear()

    elif choice2=="3":
        for key, value in rd.outer_dict.items(): # O(n)
            if value.get("course_id")[0:3]=="FSW":
                choose_function(key, value)
        sort_list_function(outer_list)
        outer_list.clear()

    else:
        print("Incorrect input")
    
#####################################################################
# 3
# This function add new student
def add_new_student_func():
    print("Adding new student")
    student_id = input("Enter the student ID:").upper()
    # Checking if the user didn't enter an ID
    if student_id =="":
        print()
        print("You should enter an ID")

    # Checking if this ID exist in the dictionary keys
    elif student_id in rd.outer_dict.keys(): # O(n)
        print()
        print("This student already exist")
        
    # Adding the details to the inner_dict
    else:
        inner_dict = {
            "first_name" : input("Enter the student first name:").lower().capitalize(),
            "last_name" : input("Enter the student last name:").lower().capitalize(),
            "course_id" : "N/A"
            }
        # Adding the details and the student_id to the outer_dict
        rd.outer_dict.update({student_id : inner_dict})
        print("Student added successfully")

#####################################################################
# 4
# This function remove a student from the dictionary
def remove_student_func():
    print("Removing existing student")
    student_id = input("Enter student ID:").upper()

    # Check if the student does not exist
    if student_id not in rd.outer_dict: # O(n)
        print("Student not found")
    else:
        rd.outer_dict.pop(student_id)
        print("Student deleted successfully")

#####################################################################
# 5
# This function is used to enroll students in courses
def enroll_existing_student_in_a_course_func():
    print("Enroll Student in course")
    student_id = input("Enter student ID:").upper()

    # Check if the student does not exist
    if student_id not in rd.outer_dict: # O(n)
        print("Student not found")
    # Check if the student is not enrolled in a course
    elif rd.outer_dict.get(student_id).get("course_id")[0:3] == "N/A":
        course_id = input("Enter the course you want to enroll it:").upper()
        rd.outer_dict[student_id]["course_id"] = course_id
        print("Course enrolled successfully")
    # Check if the student is enrolled in a course
    else:
        print("Student allready enrolled in a course")

#####################################################################
# 6
# This function is used to edit the details of students
def edit_student_func():
    print("Edit a Student details")
    student_id = input("Enter student ID:").upper()

    # Check if the student does not exist
    if student_id not in rd.outer_dict: # O(n)
        print("Student not found")
    else:
        print()
        print("Enter the new details:")
        print("If you leave it empty, the old value will not change")

        new_first_name = input("Enter the new first name:").lower().capitalize()
        if  new_first_name != "":
            rd.outer_dict[student_id]["first_name"] = new_first_name

        new_last_name = input("Enter the new last name:").lower().capitalize()
        if  new_last_name != "":
            rd.outer_dict[student_id]["last_name"] = new_last_name

        new_course_id = input("Enter the new course ID:").upper()
        if  new_course_id != "":
            rd.outer_dict[student_id]["course_id"] = new_course_id

        new_student_id = input("Enter the new student ID:").upper()
        if  new_student_id != "": 
            rd.outer_dict[new_student_id] = rd.outer_dict.pop(student_id)

#####################################################################
# 7
# This function display specific student and there informations
def display_student_func():
    print("Displaying students details:")
    info = input("Enter student ID or name:")

    # Checking if the user entered a name or ID 
    if info[0:5]=="SEFST":
        # info in this case is the student_id
        if info in rd.outer_dict: # O(n)
            print()
            print("Student ID:", info)
            print("First name:", rd.outer_dict[info]["first_name"])
            print("Last name:", rd.outer_dict[info]["last_name"])
            print("Course ID:", rd.outer_dict[info]["course_id"])
        else:
            print("Student not found")
    else:
        # info in this case is the first_name

        # this value will become True if we found at least one user having the input name
        found = False

        # Looping through outer_dict
        for key, value in rd.outer_dict.items(): # O(n)
            if value["first_name"]==info:
                print()
                print("Student ID:", key)
                print("First name:", value["first_name"])
                print("Last name:", value["last_name"])
                print("Course ID:", value["course_id"])
                found = True
        if found==False:
            print("Student not found")

#####################################################################
# 8
# This function exit the running task
def exit_func():
    print()
    print("Do you want to save your changes?")
    print("If YES press: y")
    print("If NO press any key")
    pressed_key = input()
    print()
    # This condition is used to check if the user want to save his changes or no
    if pressed_key=="y":
        # Updating the edited dictionary in the database
        file = open("database.txt", "w")
        my_str = ""
        for key, value in rd.outer_dict.items(): # O(n)
            # Concatenate the data to get the original form in my_str
            my_str += key + ": " + value["first_name"] + ", " + value["last_name"] + ", " + value["course_id"] + "\n"
        # Writting my_str to the text document without the last \n
        file.write(my_str[:-1])
        file.close()
        print("You have logged out")
        print("you have saved your changes")

    else:
        print("You have logged out")
        print("You haven't change anything")

    sys.exit() # exit the running task