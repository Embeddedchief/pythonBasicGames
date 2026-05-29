##Algorithm
#Create master password
#Create function for view
#Create function for add
#Ask for master password
#Check if it mathces the created password, if no(quit with incorrect password) if yes(continue to next step)
#Ask if user would like to add (add new password), view (view existing password) list or q(quit)


#Create master password
master_password = 'paskEy12345'

#Create function for view
def add():
    username = input("Kindly input username for the account ")
    password = input("Kindly input password for the account ")

    with open('passwordManager.txt', 'a') as f:
        f.write("username: " + str(username) + "\n" + "password: " + str(password) + "\n\n")


#Ask for master password
input_master_password = input("input your master password? ")

while True:
    #Check if it mathces the created password, if no(quit with incorrect password) if yes(continue to next step)
    if input_master_password != master_password:
        print("Incorrect password")
        quit()

    #Ask if user would like to add (add new password), view (view existing password) list or q(quit)
    answer = input("type add to add new password, view to view password and q to quit ").lower()

    if answer == 'add':
        add()
    elif answer == 'view':
        pass
    else:
        quit()