"""
This bloc is used to read the data from file and add them to the dictionary
"""

outer_dict = {}
# reading the data of students from the txt document
file = open("database.txt", "r")

# Looping through every line in the text document
for line in file: # O(n)
    # Parsing every line in the text document
    # save them in the inner_dictionary
    """
    **those three form the student_id
    symbol = line[0:5]
    inscription_year = line[5:7]
    student_num = line[7:11]
    
    first_name = line[13:line.find(",")]
    last_name = line[line.find(",")+2:line.rfind(",")]

    **those three form the course_id
    course_name = line[line.rfind(",")+2:line.rfind(",")+5]
    course_year = line[line.rfind(",")+5:line.rfind(",")+7]
    course_num = line[line.rfind(",")+7:line.rfind(",")+10]
    """
    inner_dict = {
        "first_name" : line[13:line.find(",")],
        "last_name" : line[line.find(",")+2:line.rfind(",")],
        "course_id" : line[line.rfind(",")+2:line.rfind(",")+10]
        }
    # The key of the outer_dict is the student_id
    outer_dict.update({line[0:11] : inner_dict})

file.close()