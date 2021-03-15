#Importing the necessary modules.
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
#Imports the pop up notifications widgets.
from PyQt5.QtWidgets import QMessageBox

#Imports system.
import sys

#Imports my SQL database module file.
from qjetdatabase import *

#Imports my other user windows and forgot password and emailing modules.
from memberWindow import *
from registerWindow import *
from emailValid import *
from staffWindow import *
from adminWindow import *

#Imports the hashing module to help me with hashing the password.
import hashlib
#Import os is used to generate a very random characters to produce a salt which,
#is later added with the characters of the password and hashed.
import os
import time

#showLoginWindow class is initiated which inherits from QtWidget(QtWidgets.QWidget)
class showLoginWindow(QtWidgets.QWidget):
    #Constructor is made, __init__() function to assign values to object properties or
    #other operations that are necessary to do when the objects is being created.
    #The __init__() function is called automatically every time the class is 
    #being used to create a new object.
    
    def __init__(self):
        #super() function that will make the child class inherit all the methods and properties from its parent.
        super().__init__()    
         
    def setupGuiLogin(self, loginWindow):
        #Setting the window title.
        loginWindow.setWindowTitle("Qjet - Login page")
        
        #Restricting the resize minimum and maximum window size to 900 by 700.
        loginWindow.setMinimumSize(QtCore.QSize(900, 700))
        loginWindow.setMaximumSize(QtCore.QSize(900, 700))
        
        #Setting up the QJet logo for the log in window icon. 
        icon = QtGui.QIcon()
        #Imports the qjetLogo.png from the current folders it's in and display it on the login window.
        icon.addPixmap(QtGui.QPixmap("qjetLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginWindow.setWindowIcon(icon)
        
        #Positions the QJet title to the center of the login window.
        self.centralwidget = QtWidgets.QWidget(loginWindow)

        #Creates the label title(title of the window).
        self.title = QtWidgets.QLabel(self.centralwidget)
        #Sets the login window title to the specified title.
        self.title.setText("Qjet-Login page")
        #Positions the Qjet title in the login window.
        self.title.setGeometry(QtCore.QRect(310, 10, 311, 81))
        
        #Sets up the font style, underlines and font size for the login window title.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        #Designs the login window title using all the QFont methods above.
        self.title.setFont(font)

        #Sets up the background image.
        self.background = QtWidgets.QLabel(self.centralwidget)
        #Positions the background image.
        self.background.setGeometry(QtCore.QRect(0, 0, 901, 700))
        self.background.setText("")
        #Imports the background image aviation.png from the current folders it's in.
        self.background.setPixmap(QtGui.QPixmap("aviation.png"))
        #Makes the image less blurry by importing and placing the image to scale.
        self.background.setScaledContents(True)
        self.background.setWordWrap(False)

        #Brings the title over the background, so the title isn't behind the background
        #in which case it won't be visible to the user.
        self.title.raise_()

        #Positions the username text on the login page window.
        self.labelUsername = QtWidgets.QLabel(self.centralwidget)
        self.labelUsername.setText("Username:")
        self.labelUsername.setGeometry(QtCore.QRect(240, 165, 181, 81))
         
        #Sets up the font style and font size for the username text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        #Designs the password text using all the QFont methods above.
        self.labelUsername.setFont(font)
        
        #Creates the password text on the login window.
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setText("Password:")
        #Positions the password text on the login window.
        self.labelPassword.setGeometry(QtCore.QRect(240, 345, 171, 81))
        
        #Sets up font style and font size for the password input box.
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        #Designs the password text using all the QFont methods above.
        self.labelPassword.setFont(font)
        
        #Sets up the logo in the log in window with QJet logo.
        self.logo = QtWidgets.QLabel(self.centralwidget)
        #Positions the Qjet logo in the login window.
        self.logo.setGeometry(QtCore.QRect(50, 205, 171, 181))
        self.logo.setText("")
        #Imports the qjetLogo.png from the current folders it's in.
        self.logo.setPixmap(QtGui.QPixmap("qjetLogo.png"))
        #Makes the image less blurry by importing and placing the image to scale.
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        
        #Creates the username user input box.
        self.editUsername = QtWidgets.QLineEdit(self.centralwidget)
        #Positions the username user input box in the login window.
        self.editUsername.setGeometry(QtCore.QRect(430, 175, 351, 61))
        
        #Sets up the font style and font size of the username user input box.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)

        #Designs up the username user input box using all the QFont methods above.
        self.editUsername.setFont(font)
        
        #Creates the password user input box.
        self.editPassword = QtWidgets.QLineEdit(self.centralwidget)
        #Positions the password user input box.
        self.editPassword.setGeometry(QtCore.QRect(430, 355, 351, 61))
        
        #Sets up the font style and font size for the password user input box.
        font.setFamily("Segoe Print")
        font.setPointSize(12)

        #Designs the password user input box using all the QFont methods above.
        self.editPassword.setFont(font)
        
        #Makes the password invisible to the user when entered.
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        
        #Creates the login button and sets the size(dimensions) of the button.
        self.buttonLogin = QtWidgets.QPushButton(self.centralwidget)
        #Sets the text of the login button.
        self.buttonLogin.setText("Login")
        #Positions the login button.
        self.buttonLogin.setGeometry(QtCore.QRect(620, 490, 161, 71))

        #Imports the Qjet logo and displays it on the login button.
        self.buttonLogin.setIcon(QtGui.QIcon("qjetLogo.png"))
        #Sets the size of the Qjet logo on the login button.
        self.buttonLogin.setIconSize(QtCore.QSize(50, 50))
        #Shows a tooltip(Text popping up showing text) when hovered over the login button.
        self.buttonLogin.setToolTip("<h3>This will take you to the next page.<h3>")

        #Sets up font style and font size for the login button.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        #Designs the login button using all the QFont methods above.
        self.buttonLogin.setFont(font)
        #Creates an blue outline for the login button which glows when hovered over.
        self.buttonLogin.setDefault(True)
        
        #When the login button is clicked the ValidateLogin method is run.
        self.buttonLogin.clicked.connect(self.ValidateLogin)
        
        #Creates the check box and sets the size(dimensions) of the check box.
        #Creates the check box to show and view password.
        self.checkBoxShowPassword = QtWidgets.QCheckBox(self.centralwidget)
        #Sets the text of the check box.
        self.checkBoxShowPassword.setText("Show password")
        #Positions the check box in the login window.
        self.checkBoxShowPassword.setGeometry(QtCore.QRect(430, 420, 321, 41))
        
        #Using the state change function, to checks if the check box is ticked to show and hide password.
        #If the check box is ticked or unticked the ShowPassword method will be run.
        self.checkBoxShowPassword.stateChanged.connect(self.ShowPassword)
                                
        #Sets up the font style and font size for the checkbox.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        
        #Designs the check box using all the QFont methods above.
        self.checkBoxShowPassword.setFont(font)

        #Creates the register button and sets the size(dimensions) of the button.
        self.buttonRegister = QtWidgets.QPushButton(self.centralwidget)
        #Sets the text of the register button.
        self.buttonRegister.setText("Register")
        #Adds the colour of the background and the text colour for the register button.
        self.buttonRegister.setStyleSheet("background-color: #2094ed; color: white")
        #Positions the register button.
        self.buttonRegister.setGeometry(QtCore.QRect(430, 490, 161, 71))
        self.buttonRegister.setDefault(True)
                
        #Sets up the font style and size for the register button.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        #Designs the login button using all the QFont methods above.
        self.buttonRegister.setFont(font)
        #When the user clicks the register button, it goes to SwitchWindowRegister and then switches to register page.
        self.buttonRegister.clicked.connect(self.switchWindowRegister)
        
        #Creates the forget password button.
        self.buttonForgotPassword = QtWidgets.QPushButton(self.centralwidget)
        self.buttonForgotPassword.setText("Forgot password?")
        #Adds the colour of the background and the text colour for the forgot password button.
        self.buttonForgotPassword.setStyleSheet("background-color: #2094ed; color: white")
        self.buttonForgotPassword.setGeometry(QtCore.QRect(60, 490, 311, 71))
        self.buttonForgotPassword.setDefault(True)

        #Sets up the font style and font size for the forgot password button.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        #Creates the loading bar in the login page.
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        #Sets the size (dimensions) of the login bar.
        self.progressBar.setGeometry(QtCore.QRect(10, 0, 881, 23))
        self.progressBar.setProperty("value", 0)

        #Designs the forget password button using all the QFont methods above.
        self.buttonForgotPassword.setFont(font)
        #When the user clicks the register button it takes to the SwitchEmail method and then switches the window to email
        #reseter window.
        self.buttonForgotPassword.clicked.connect(self.switchEmailWindow)
        
        #Makes all thw widgets alligned and ceneter of the set window size.
        loginWindow.setCentralWidget(self.centralwidget)
    
    #This function shows and hide password.
    def ShowPassword(self, state):
        #Using the state function it checks if states has changed (If the check box is clicked or not).
        if state == Qt.Checked:
            #If the check box is ticked, it shows the password and gives the option to hide password.
            self.editPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.editPassword.setText(self.editPassword.text())
            #Changes the checkbox text to hide password.
            self.checkBoxShowPassword.setText("Hide password")
        else:
            #Else it hides the password and gives he option to show password.
            self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
            self.editPassword.setText(self.editPassword.text())
            #Changes the chekbox text to show password.
            self.checkBoxShowPassword.setText("Show password")
    
    #Queries the database for email and password for member, staff and admin.
    def ValidateLogin(self):
        #Specifies the location of the database.
        database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
        #Creates the database connection.
        connection = CreateConnection(database)
        #Creates the cursor object by calling the cursor() function method of the connection object.
        c = connection.cursor()

        #Executes a SQL statement to retrieve Email from the Member table..
        c.execute("SELECT Email FROM Member")
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()
        print(data)
        #Creates a memberEmail list, so email addresses can be appeneded after a list comprehension is performed
        #on the data retrieved as arrays.
        memberEmail = []

        #Gets the data from the database as arrays and performs a list comprehension and stores the email addresses in a list.
        for email in data:
            for emailList in email:
                #Appends the email to the memberEmail list.
                memberEmail.append(emailList)
        print(memberEmail)
        
        #Executes a sql statement to retrieve Password from Member table.
        c.execute("SELECT Hash FROM Member")
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a memberPassword list, so passwords can be appeneded after a list comprehension is performed
        #on the data retrieved as arrays.
        memberHash = []

        #Gets the data from the database as arrays and performs a list comprehension and stores the member passwords in a list.
        for hash in data:
            for hashList in hash:
                #Appends the password to the memberPassword list.
                memberHash.append(hashList)

        #Executes a sql statement to retrieve MemberID from Member where using the email inputed by the user at the login page.
        c.execute("SELECT MemberID FROM Member WHERE Email = ?", [self.editUsername.text().strip()])
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a memberID list, so memberID can be appeneded after a list comprehension is performed
        #on the data retrieved as arrays.
        memberID = []

        #Gets the data from the database as arrays and performs a list comprehension and stores the member id in a list.
        for ID in data:
            for memberIDList in ID:
                #Appends the memberID to to the memberID list.
                memberID.append(memberIDList)
        
        #Checks if the memberID list is empty.
        if not memberID:
            print("MemberID list is empty.") 
        #Otherwise sendMemberID is assigend to the first and only item in the memberID list.
        #sendMemberID is later used in the member page to retrieve details.
        #sendMemberID is later used in the cancel/ book page.
        else:
            #First item in the memberID list is assigned to the variable sendMemberID.
            #There will be only one item in the memberID list as I will be using the email address
            #to query for the memberID in the member table.
            sendMemberID = memberID[0]
                        
        #Executes a sql statement to retrieve the email from the Staff table.   
        c.execute("SELECT Email FROM Staff")
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a staffEmail list, so email addresses can be appeneded after a list comprehension is performed
        #on the data retrieved as arrays.
        staffEmail = []

        #Gets the data from the database as arrays and performs a list comprehension and stores the staff emails in a list.
        for email in data:
            for emailList in email:
                #Appends the email to the staffEmail list.
                staffEmail.append(emailList)
        
        #Exeutes a sql statement to retrieve the password from Staff table.
        c.execute("SELECT Hash FROM Staff")
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a staffPassword list, so passwords can be appeneded after a list comprehension is performed
        #on the data retrieved as arrays.
        staffHash= []

        #Gets the data from the database as arrays and performs a list comprehension and stores staff paswords in a list.
        for hash in data:
            for hashList in hash:
                #Appends the password to the staffPassword list.
                staffHash.append(hashList)
        
        #Executes a sql statement to retrieve the staffID from the Staff table where using the inputed email in the login window.        
        c.execute("SELECT StaffID FROM Staff WHERE Email = ?", [self.editUsername.text().strip()])
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a staffID list, so staffID can be appeneded after a list comprehension is performed
        #on the data retrieved as arrays.
        staffID = []
        
        #Gets the data from the database as arrays and performs a list comprehension and stores staff id in a list.
        for ID in data:
            for staffIDList in ID:
                staffID.append(staffIDList)

        #Checks if the staffID list is empty.
        if not staffID:
            print("StaffID list is empty.") 
        #Otherwise staffID is assigend to the first and only item in the staffID list.
        #sendStaffID is later used in the staff page to retrieve details.
        #sendStaffID is later used in the cancel/ book page.    
        else:
            #First item in the staffID list is assigned to the variable sendStaffID.
            #There will be only one item in the staffID list as I will be using the email address
            #to query for the staffID in the staff table.
            sendStaffID = staffID[0]

        #Executes a sql statement to retrieve the email from the Staff table.   
        c.execute("SELECT Email FROM Admin")
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a staffEmail list, so email addresses can be appeneded after a list comprehension is performed
        #on the data retrieved as arrays.
        adminEmail = []

        #Gets the data from the database as arrays and performs a list comprehension and stores the staff emails in a list.
        for email in data:
            for emailList in email:
                #Appends the email to the staffEmail list.
                adminEmail.append(emailList)
        
        #Exeutes a sql statement to retrieve the password from Staff table.
        c.execute("SELECT Hash FROM Admin")
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a staffPassword list, so passwords can be appeneded after a list comprehension is performed
        #on the data retrieved as arrays.
        adminHash = []

        #Gets the data from the database as arrays and performs a list comprehension and stores staff paswords in a list.
        for hash in data:
            for hashList in hash:
                #Appends the password to the staffPassword list.
                adminHash.append(hashList)
        
        #Executes a sql statement to retrieve the staffID from the Staff table where using the inputed email in the login window.        
        c.execute("SELECT AdminID FROM Admin WHERE Email = ?", [self.editUsername.text().strip()])
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a staffID list, so staffID can be appeneded after a list comprehension is performed
        #on the data retrieved as arrays.
        adminID = []

        #Gets the data from the database as arrays and performs a list comprehension and stores staff id in a list.
        for ID in data:
            for adminIDList in ID:
                adminID.append(adminIDList)

        #Checks if the staffID list is empty.
        if not adminID:
            print("AdminID list is empty.") 
        #Otherwise staffID is assigend to the first and only item in the staffID list.
        #sendStaffID is later used in the staff page to retrieve details.
        #sendStaffID is later used in the cancel/ book page.    
        else:
            #First item in the staffID list is assigned to the variable sendStaffID.
            #There will be only one item in the staffID list as I will be using the email address
            #to query for the staffID in the staff table.
            sendAdminID = adminID[0]

        c.execute("SELECT Salt FROM Member")
        data = c.fetchall()
        
        saltMember = []

        for salt in data:
            for saltList in salt:
                saltMember.append(saltList)

        print("Member", saltMember)

        c.execute("SELECT Salt FROM Staff")
        data = c.fetchall()
        
        saltStaff = []

        for salt in data:
            for saltList in salt:
                saltStaff.append(saltList)
        print("Staff", saltStaff)

        c.execute("SELECT Salt FROM Admin")
        data = c.fetchall()
        
        saltAdmin = []

        for salt in data:
            for saltList in salt:
                saltAdmin.append(saltList)
        print("Admin", saltAdmin)

        
        #Boolean to check if it's member, staff or admin.
        hashStateDict = {
        "isItMember": "False",
        "saveMemberHash": "",
        "isItStaff": "False",
        "saveStaffHash": "",
        "isItAdmin": "False",
        "saveAdminHash": ""
        }

        print(hashStateDict)

        #Hashes the user inputted password.
        #Hashing
        for i in range(len(saltMember)):
            inputPassword = self.editPassword.text()
            #Converts the text to binary(bytes).
            passwordEncode = inputPassword.encode()
            print("Encoded:", passwordEncode)

            saltDecode = bytearray.fromhex(saltMember[i])
            #Hashes the salt generated + the password entered by the user.
            #Decodes the salt hex from the database to bytes
            hashPassword = hashlib.pbkdf2_hmac("sha256", passwordEncode, saltDecode, 100000)
            #Converts the binary(bytes) into hex so easily readable and saves space in the database. 
            hashPasswordHex = hashPassword.hex()
            print("Hashed password(hex):", hashPasswordHex)

            if hashPasswordHex in memberHash:
                hashStateDict["isItMember"] = "True"
                hashStateDict["saveMemberHash"] = hashPasswordHex
            else:
                pass

        #Hashes the user inputted password.
        #Hashing
        for i in range(len(saltStaff)):
            inputPassword = self.editPassword.text()
            #Converts the text to binary(bytes).
            passwordEncode = inputPassword.encode()
            print("Encoded:", passwordEncode)

            saltDecode = bytearray.fromhex(saltStaff[i])
            #Hashes the salt generated + the password entered by the user.
            #Decodes the salt hex from the database to bytes
            hashPassword = hashlib.pbkdf2_hmac("sha256", passwordEncode, saltDecode, 100000)
            #Converts the binary(bytes) into hex so easily readable and saves space in the database. 
            hashPasswordHex = hashPassword.hex()
            print("Hashed password(hex):", hashPasswordHex)

            if hashPasswordHex in staffHash:
                hashStateDict["isItStaff"] = "True"
                hashStateDict["saveStaffHash"] = hashPasswordHex
            else:
                pass

        #Hashes the user inputted password.
        #Hashing
        for i in range(len(saltAdmin)):
            inputPassword = self.editPassword.text()
            #Converts the text to binary(bytes).
            passwordEncode = inputPassword.encode()
            print("Encoded:", passwordEncode)

            saltDecode = bytearray.fromhex(saltAdmin[i])
            #Hashes the salt generated + the password entered by the user.
            #Decodes the salt hex from the database to bytes
            hashPassword = hashlib.pbkdf2_hmac("sha256", passwordEncode, saltDecode, 100000)
            #Converts the binary(bytes) into hex so easily readable and saves space in the database. 
            hashPasswordHex = hashPassword.hex()
            print("Hashed password(hex):", hashPasswordHex)

            if hashPasswordHex in adminHash:
                hashStateDict["isItAdmin"] = "True"
                hashStateDict["saveAdminHash"] = hashPasswordHex
                print(hashStateDict)
            else:
                pass

        #Using nested if it checks if the username and password matches with each other, making it more secure.
        #Also if the username contains a email address (@) and the password is greater than 8 characters long.
        #The username(email) that is inputted by the user is striped of any spaces and checked against the database.
        if (len(self.editUsername.text().strip()) >= 8 and "@" in self.editUsername.text().strip() and
            len(self.editPassword.text()) >= 8):
            #After the first check being it checks if the email is greater than or equal to 8 characters long
            #and contains @ AND the password is greater than or equal to 8 characters.
            #The username(email) will be checked to see if it's valid and this is done by checking if it's in the memberEmail list
            #which contains the email addresses from the member table.
            #The password will be checked by checking if it's in the memberPassword list.
            if (self.editUsername.text().strip() in memberEmail and hashStateDict["isItMember"] == "True"
                and memberEmail.index(self.editUsername.text()) == memberHash.index(hashStateDict["saveMemberHash"])):
                print("Correct")
                #If the username(email) and password is in the necessaray list the correct pop up notification for the user will
                #up.
                self.showPopupDetailsCorrect("You have successfully logged on.")
                #The member id is also passed into the switchWindowMember method so it's recieved as an arguement in the memberWindow
                #module.
                self.switchWindowMember(sendMemberID)

            elif (self.editUsername.text().strip() in staffEmail and hashStateDict["isItStaff"] == "True"
                and staffEmail.index(self.editUsername.text()) == staffHash.index(hashStateDict["saveStaffHash"])):
                print("Staff")
                self.showPopupDetailsCorrect("You have successfully logged on as staff.")
                self.switchStaffWindow(sendStaffID)

            elif (self.editUsername.text().strip() in adminEmail and hashStateDict["isItAdmin"] == "True"
                and adminEmail.index(self.editUsername.text()) == adminHash.index(hashStateDict["saveAdminHash"])):
                print("Admin")

                #The loading bar timer starts.
                self.timer = QTimer()
                #Connects with the handleTimer method below to work out how fast to progress the loading bar.
                self.timer.timeout.connect(self.handleTimer)
                self.timer.start(10)

                #The method handleTimer is run.
                self.handleTimer()

                self.showPopupDetailsCorrect("You have successfully logged on as admin.")
                self.switchAdminWindow(sendAdminID)
            
            #If the username and password aren't in the staff, member or admin email and password lists
            #it jumps to the else statement outputting an error to console. Also pop ups the notification
            #to the user.
            else:
                print("Details doesn't exist in member, staff or table.")
                self.showPopupDetailsIncorrect()
        #Else statement is executed when the if the username and password does't meet the minimum
        #length requirements and if the username (email) doesn't contain the "@" symbol.        
        else:
            print("Doesn't meet the conditions for length and special characters.")
            #showPopupDetailsIncorrect method is run and this pop ups a notification to the user
            #explaning what went wrong.
            self.showPopupDetailsIncorrect()

    #This workouts the how fast to progress the loading bar, so it can be accurately worked
    #out in the login page.
    def handleTimer(self):
        value = self.progressBar.value()
        if value < 100:
            value = value + 1
            self.progressBar.setValue(value)
        else:
            #Once the loading bar as reached 100% it will reset back to 0%
            self.timer.stop()
            self.progressBar.setProperty("value", 0)

    #When the login details are correct for member, staff or admin the pop up notification will be shown to the user which is in
    #this method and this method recieves info as arguement where it will contain for exmaple if the member is logging in
    # "You have sucessfully logged in as member".
    def showPopupDetailsCorrect(self, info):
        message = QMessageBox()
        #Set the pop up title text to the specified text.
        message.setWindowTitle("Successful")
        #Sets the main note text for the pop up such as "You have sucessfully logged in as member".
        message.setText(info)
        #Sets the pop up incon to a information icon.
        message.setIcon(QMessageBox.Information)

        #Places a "Ok" button
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        x = message.exec_()
        #At this stage the user will be validated against the database.
        #So the username and password user input fields will be reset to blank.
        self.editUsername.setText("")
        self.editPassword.setText("")

    #When the login details, username or password are wrong when checked against the database, this pop up notification
    #is popped up tot the user.
    def showPopupDetailsIncorrect(self):
        message = QMessageBox()
        message.setWindowTitle("Unsuccessful")
        message.setText("Incorrect username(email) or password.")
        message.setIcon(QMessageBox.Warning)
        message.setDetailedText("Your details doesn't exist in our database.")

        message.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        x = message.exec_()

    #When the login details, username and password is correct and validated against the database.
    #This method is ran which will recieve "sendMemberID" as an arguement.
    #This method is use to switch the user from the login page to the member page which
    #is in a separate module.
    def switchWindowMember(self, sendMemberID):
        #sendMemberID is assigned to the instance variable (self.sendMemberID) so it can be passed on to the member page
        #as a parameter which in the member page can be used to get all the details of the user logging in.
        self.sendMemberID = sendMemberID
        #The member page is intialised.
        self.memberWindow = QtWidgets.QMainWindow()
        #The sendMemberID which contains the 4 digit member ID is passed on to the member page as parameter.
        self.switch = showMemberWindow(self.sendMemberID)
        #The GUI and widgets are set up and then the page is ready to show/ switch.
        self.switch.setupGuiMember(self.memberWindow)
        #The member page will be switched and shown to the user.
        self.memberWindow.show()

    #When the login details are validated against the database and is recognised as a staff, this method will be run to switch the
    #user from the login page to staff page.
    def switchStaffWindow(self, sendStaffID):
        self.sendStaffID = sendStaffID
        self.staffWindow = QtWidgets.QMainWindow()
        self.switch = showStaffWindow(self.sendStaffID)
        self.switch.setupGuiStaff(self.staffWindow)
        self.staffWindow.show()

    #When the login details are validated against the database and is recoginsed as an admin, this method will be run to switch the
    #user from the login page to the admin page.
    def switchAdminWindow(self, sendAdminID):
        self.sendAdminID = sendAdminID
        self.adminWindow = QtWidgets.QMainWindow()
        self.switch = showAdminWindow(self.sendAdminID)
        self.switch.setupGuiAdmin(self.adminWindow)
        self.adminWindow.show()

    #When the user clicks the "Register" button, this method will be run to switch the user from the login page to the
    #register page.
    def switchWindowRegister(self):
        self.registerWindow = QtWidgets.QMainWindow()
        self.switch = showRegisterWindow()
        self.switch.setupGuiRegister(self.registerWindow)
        self.registerWindow.show()
 
    #When the user clicks "Forgot password" button, this method will be run to switch the user from the login page to the
    #reseet password page.
    def switchEmailWindow(self):
        self.emailWindow = QtWidgets.QMainWindow()
        self.switch = showEmailWindow()
        self.switch.setupGuiEmail(self.emailWindow)
        self.emailWindow.show()
   
#The showLoginWindow is intialised and shown to the user by default when the program is run.                    
if __name__ == "__main__":
    #Sets up the QWidgets and core applications to set up and run the page.
    app = QtWidgets.QApplication(sys.argv)
    #loginWindow is defined by QtWidgets which will be run to initialise the GUI and widgets.
    loginWindow = QtWidgets.QMainWindow()
    #The login window class is assigned to the variable GUI.
    gui = showLoginWindow()
    #The login page is setup and the "setupGuiLogin" is run which is used to show the page.
    gui.setupGuiLogin(loginWindow)
    #The login page is shown.
    loginWindow.show()
    #When the user wants to clsoe the login page, its closed.
    sys.exit(app.exec_())
    
#Total = 4K+ lines of code.
