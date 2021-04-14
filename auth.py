# register
# - username,password,email
# generate user account


# login
# accountnumber and password


# Bank Operations
# withdrawal,deposit,enquiries
import random


database = {}


def init():

    print("Welcome to bankPHY")

    haveAccount = int(input("do you have an account with us: 1 (yes) 2 (no) \n"))

    if (haveAccount == 1):
            
        login()
    elif (haveAccount == 2):
           
        register()
    else:
            print("You have selected an invalid option")
            init()

def login():
    print("*******Login*******")

    accountNumberFromUser = int(input("Please Enter your Account Number: \n"))
    password = input("Enter your password: \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)



    print('Invalid account or password')
    login()

def register():

    print("*********** Please Register **********")

    email = input("Please Enter your email address: \n")
    first_name = input("Enter your First Name: \n")
    last_name = input("Enter your Last Name: \n")
    password = input("Create a password:  \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Hi %s Your Account has been created" % first_name)
    print("==============================================")
    print("This is your account Number: %d" % accountNumber)
    print("Please keep it safe")
    print("==============================================")

    login()


def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    selectedOption = int(input(
        "What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))
    if(selectedOption == 1):
        depositOperation()

    elif (selectedOption == 2):
        withdrawalOperation()

    elif (selectedOption == 3):
        logout()

    elif (selectedOption == 4):
        exit()

    else:
        print("You selected an invalid Option")
        bankOperation(user)


def depositOperation():
    print("This is a deposit Operation")


def withdrawalOperation():
    print("This is a withdrawal Operation")


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def logout():
    login()
### ACTUAL BANKING SYSTEM ####
init()
