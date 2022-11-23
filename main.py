"""
This is the main page
it contains the login details
"""
import menu

# Using a dictionary because we may have multiple username and password
login_dict = {
    "admin": "admin123123",
    "a": "a"
    }

print("Welcome to our Student Management System")
print()

# Giving 5 chances to enter a correct username and password
i=0
while i<5: # O(1)
    print("attempts you have:", 5-i)
    username = input("Enter your username:")
    password = input("Enter your password:")
    print()
    # if the username and password are correct
    if username in login_dict.keys() and password==login_dict[username]: # O(n)
        menu.return_function()
    i+=1