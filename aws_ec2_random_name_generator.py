import random           # Import module to generate random names

import string           # Import module that provides letters and digits for random name generation

# list of allowed departments to use this generator 
allowed_departments = ['marketing', 'accounting', 'finops']

# Ask the user how many EC2 instances they want to name 
ec2_instances = int(input("How many EC2 instances do you want to name?\n: "))

department_name = input("Enter your department: ")

department_name = department_name.lower()  # Convert department name to lowercase for comparison

# Check if the department name is in the list of allowed departments
if department_name not in allowed_departments:
    #Inform the user that their department is not approved
    print("Sorry, this generator is only for the following departments:")
    for dept in allowed_departments:
        print(f"- {dept}")
    exit(1)         # Exit the program if the department is not approved

for i in range(ec2_instances):
    # Generate a 6 character random uppercase letters
    random_letters = ''.join(random.choices(string.ascii_uppercase, k=6))
    # Generate a 4 digit random number
    random_digits = ''.join(random.choices(string.digits, k=4))
    # Build the random name by combining department name and random letters
    ec2_name = department_name.capitalize() + '-' + random_letters + '-' + random_digits
    print(ec2_name)