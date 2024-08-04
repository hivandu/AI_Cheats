# Define data variables to store registered user information
userdict = {}  # Dictionary to store all usernames and passwords
userlist = []  # List to store all usernames
blackUserList = []  # List for blacklisted users

# Define a function to read all user data
def readAllUsers():
    # Read all registration information
    with open('./data/user.txt', 'a+', encoding="utf-8") as fp:
        global userdict
        global userlist
        fp.seek(0,0)  # Move pointer to the beginning of the file
        res = fp.readlines()  # Read all user data line by line
        for i in res:  # Loop through each line of data
            r = i.strip()  # Remove newline characters from each line
            mydict = r.split(':')
            userdict.update({mydict[0]:mydict[1]})
            userlist = userdict.keys()

    # Read all blacklisted users
    with open('./data/black.txt', 'a+', encoding='utf-8') as fp:
        global blackUserList
        fp.seek(0,0)
        res = fp.readlines()
        for i in res:
            r = i.strip()
            blackUserList.append(r)

# Define a function to handle registration
def register():
    # Define a variable to control the outer loop
    site = True
    # Loop for username operation
    while site:
        # Get the username input from the user
        username = input('Welcome to register, please enter your username: ')

        # Check if the username already exists
        if username in userlist:
            print('The username already exists, please choose another one.')
        else:
            # Loop until everything is correct
            while True:
                # Get the password input from the user
                password = input('Please enter your password: ')
                
                # Check if the password length is at least 6 characters
                if len(password) >= 6:
                    # Confirm your password
                    re_password = input('Please enter your password again: ')
                    # Check if the password and confirmation match
                    if re_password == password:
                        # Username and password are correct, write to file
                        with open('./data/user.txt', 'a+', encoding='UTF-8') as fp:
                            fp.write(f'{username}:{password}\n')
                        print(f'Registration successful: Username: {username}')
                        # End the loop
                        site = False
                        break
                    else:
                        print('The passwords do not match, please try again.', username, password, re_password)

                # Password length is insufficient
                else:
                    print('Password format is incorrect:', username, password)

# Define a function to handle login
def login():
    # Custom variable to control the login loop
    isLogin = True
    # Define a variable to count the number of password errors
    errorNum = 3

    # Create loop
    while isLogin:
        # Get the username input from the user
        username = input('Welcome to login, please enter your username: ')
        
        # Check if the username is in the blacklist
        if username in blackUserList:
            print('Your account has been locked and you have not yet provided a tribute to the administrator.')
            isLogin = False  # End the outer loop
        elif username in userlist:
            while True:
                # Get the password input from the user
                pwd = input('Please enter your password: ')
                # Check if the entered password is correct
                if pwd == userdict[username]:
                    print(pwd)
                    isLogin = False  # End the outer loop
                    break  # End the inner loop
                else:
                    # Password error, decrement error count
                    errorNum -= 1
                    # Check current password error count
                    if errorNum == 0:
                        print('You were given a chance and you still failed. Account is locked. Please contact the administrator and provide a tribute.')
                        # Lock the current account and add the user to the blacklist
                        with open('./data/black.txt', 'a+', encoding='UTF-8') as fp:
                            fp.write(username+'\n')
                        isLogin = False
                        break
                    else:
                        print(f'Your password is incorrect. You have {errorNum} attempts remaining.')
        else:
            # Username does not exist
            print('Username error, please try again.')

# Check if the script is being run as the main program
if __name__ == '__main__':
    '''
    The code here will only execute when the script is run directly with the Python interpreter.
    If the script is imported as a module into another file, this code will not run.
    Therefore, this is a good place to write some tests for the current script, as it will not affect other scripts.
    '''
    # Call the initialization method to load data
    readAllUsers()
    
    isBegin = True
    while isBegin:
        myStr = '''
        ======================
        ** Login (0) Register (1)**
        ======================
        '''
        print(myStr)

        # Prompt the user to choose an option
        num = input('Please enter the corresponding number to use the feature: ')
        if num == '0':
            login()
            isBegin = False
        elif num == '1':
            register()
            isBegin = False
        else:
            print('Subsequent features are still under development.')
            isBegin = False