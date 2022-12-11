# Import the dependencies
import sys

# Add a master password
MASTER_PASSWORD = 12345
# Take a password as input
password = input('Please enter your password: ')

# Keep track of the number of password attempts
attempt_count = 1

# While the password is incorrect and there has been less than 3 attempts, ask for the password until it is valid
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit('Too many invalid attempts')
    password = input('Invalid password, please try again: ')
    attempt_count += 1
print('Thank you! Welcome to Your Account')
