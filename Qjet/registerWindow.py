#Importing the necessary modules.
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
#Imports the pop up notifications widgets.
from PyQt5.QtWidgets import QMessageBox

#Imports the system module.
import sys

#Imports the other python files that I made as modules.
#Imports my database file.
from qjetdatabase import *

#Imports my login window module.
from loginWindow import *

#Import the random module.
import random
#Imports the the randint function from the random module.
from random import randint
#Imports the RegEx module.
import re

#Imports the hashlib module, which is used to help me hash the password.
import hashlib
#Imports the OS module, so it can be used to generate a arbitrary charatcers
#for my salt which is uniquely generated for each new password entered.
import os

#showRegisterWindow class is initiated which inherits from QtWidget(QtWidgets.QWidget).
class showRegisterWindow(QtWidgets.QWidget):
    #Constructor is made, __init__() function to assign values to object properties or
    #other operations that are necessaeay to do when the objects is being created.
    #The __init__() function is called automatically every time the class is 
    #being used to create a new object.

    #This constructor recieves sendAdminID as a paramater from the
    #login window(loginWindow).
    #The self parameter is a reference to the current instance of the class,
    #and is used to access variables that belong to the class.
    def __init__(self):
        #super() function that will make the child class inherit all the methods and properties from its parent.
        super().__init__()
        #The self parameter is a reference to the current instance of the class,
        #and is used to access variables that belongs to the class.
    
    #Objects can also contain methods. Methods in objects are functions that belong to the object.
    def setupGuiRegister(self, registerWindow):
        #Setting the window title.
        registerWindow.setWindowTitle("QJet-Register Page")
        registerWindow.resize(800, 600)
        #Restricting the resize minimum and maximum window size to 900 by 700.
        registerWindow.setMinimumSize(QtCore.QSize(900, 700))
        registerWindow.setMaximumSize(QtCore.QSize(900, 700))
        
        #Positions the register title to the center of the register window.
        self.centralwidget = QtWidgets.QWidget(registerWindow)
        
        #Creates the title in the register window.
        self.title = QtWidgets.QLabel(self.centralwidget)
        #Sets the title text.
        self.title.setText("QJet - Register Page")
        #Positions the Qjet title in the register window.
        self.title.setGeometry(QtCore.QRect(240, 0, 351, 81))
        
        #Sets up the font style, underlines and font size for the title text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        #Setting up the QJet logo for the log in window icon. 
        icon = QtGui.QIcon()
        #Imports the qjetLogo.png from the current folders it's in and display it on the login window.
        icon.addPixmap(QtGui.QPixmap("qjetLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        registerWindow.setWindowIcon(icon)
    
        #Designs the login window title using all the QFont methods above.
        self.title.setFont(font)

        #Sets up the background image.
        self.background = QtWidgets.QLabel(self.centralwidget)
        #Positions the background image.
        self.background.setGeometry(QtCore.QRect(0, 0, 901, 700))
        self.background.setText("")
        #Imports the aviation.png from the current folders it's in.
        self.background.setPixmap(QtGui.QPixmap("aviation.png"))
        #Makes the image less blurry by importing and placing it to scale.
        self.background.setScaledContents(True)
        self.background.setWordWrap(False)

        #Brings the title front over the background.
        self.title.raise_()
        
        #Creates a text label called "Firstname:" in the register window.
        self.firstName = QtWidgets.QLabel(self.centralwidget)
        self.firstName.setText("Firstname:")
        #Sets the dimensions (size and positions) in the register window.
        self.firstName.setGeometry(QtCore.QRect(190, 80, 181, 81))
        
        #Sets up the font style, underlines and font size for the text that says "Firstname:".
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        #Designs the register window "Firstname:" text using all the QFont methods above.
        self.firstName.setFont(font)
        
        #Creates a text label called "Suname:".
        self.surname = QtWidgets.QLabel(self.centralwidget)
        self.surname.setText("Surname:")
        self.surname.setGeometry(QtCore.QRect(190, 160, 181, 81))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        self.surname.setFont(font)
        
        #Creates a text label called "Mobile number:".
        self.mobileNumber = QtWidgets.QLabel(self.centralwidget)
        self.mobileNumber.setText("Mobile number:")
        self.mobileNumber.setGeometry(QtCore.QRect(190, 320, 181, 81))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        self.mobileNumber.setFont(font)
        
        #Creates a text label called "Email:".
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setText("Email:")
        self.email.setGeometry(QtCore.QRect(190, 240, 181, 81))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        self.email.setFont(font)
        
        #Creates a text label called "Password:".
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setText("Password:")
        self.password.setGeometry(QtCore.QRect(190, 400, 181, 81))

        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        self.password.setFont(font)

        #Creates the check box for show and hide password.
        self.checkBoxShowPassword = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxShowPassword.setText("Show password")
        self.checkBoxShowPassword.setGeometry(QtCore.QRect(380, 460, 321, 101))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        
        self.checkBoxShowPassword.setFont(font)
        
        #Using the state change function, it checks if the check box is ticked to show and hide password.
        self.checkBoxShowPassword.stateChanged.connect(self.showPassword)
        
        #Creates the user input to enter the first name.
        self.editFirstname = QtWidgets.QLineEdit(self.centralwidget)
        #Positions the the user input box of text and sets the size(dimensions).
        self.editFirstname.setGeometry(QtCore.QRect(370, 90, 351, 61))
        
        #Sets up the font style, underlines and font size for the text that will be inputted by the user.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)

        #Designs the text inputted by using all the QFont methods above.
        self.editFirstname.setFont(font)
        
        #Creates the user input to enter the surname.
        self.editSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.editSurname.setGeometry(QtCore.QRect(370, 170, 351, 61))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        
        self.editSurname.setFont(font)
        
        #Creates the user input to enter the email.
        self.editEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.editEmail.setGeometry(QtCore.QRect(370, 250, 351, 61))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        
        self.editEmail.setFont(font)
        
        #Creates the user input to enter the mobile number.
        self.editMobileNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.editMobileNumber.setGeometry(QtCore.QRect(370, 330, 351, 61))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        
        self.editMobileNumber.setFont(font)
        
        #Creates the user input to enter the password.
        self.editPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.editPassword.setGeometry(QtCore.QRect(370, 410, 351, 61))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        
        #Makes the password invisible to the user when entered.
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPassword.setFont(font)
        
        #Creates the reigster button.
        self.buttonRegister = QtWidgets.QPushButton(self.centralwidget)
        #Sets the button text.
        self.buttonRegister.setText("Register")
        #Positions the register button and sets the size(dimensions).
        self.buttonRegister.setGeometry(QtCore.QRect(190, 480, 161, 61))
        #Creates an blue outline for the register button which glows when hovered over.
        self.buttonRegister.setDefault(True)
        
        #Sets up the font style, underlines and font size for the register button.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        #Designs the register window Logout button text using all the QFont methods above.
        self.buttonRegister.setFont(font)
        
        #When the "Register" button is clicked, "detailsValidator" method is run.
        self.buttonRegister.clicked.connect(self.detailsValidator)
        
        #Creates the "Back" button.
        self.buttonBack = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBack.setText("Back")
        self.buttonBack.setGeometry(QtCore.QRect(10, 480, 161, 61))

        self.buttonBack.setDefault(True)

        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.buttonBack.setFont(font)
        
        #When user clicks to back, this takes them to the login window.
        self.buttonBack.clicked.connect(lambda:self.switchWindowLogin(registerWindow))
        
        registerWindow.setCentralWidget(self.centralwidget)
  
     #This function shows and hide password.
    def showPassword(self, state):
        #Using the fuctiom state it checks if states has changed.
        if state == Qt.Checked:
            #If the check box is ticked, it shows the password and gives the option to hide password.
            self.editPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.editPassword.setText(self.editPassword.text())
            #Changes the chekbox text to hide password.
            self.checkBoxShowPassword.setText("Hide password")
        else:
            #Else it hides the password and gives he option to show password.
            self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
            self.editPassword.setText(self.editPassword.text())
            #Changes the chekbox text to show password.
            self.checkBoxShowPassword.setText("Show password")

    #Generates a 4 digit unqiue Member ID using a recursion method.
    def recursionGenerateID(self, generateID):
        #Converts the integer number recieved as parameter to string, so more numbers can be appended.
        self.generateID = str(generateID)
        #If the generatedID is less than 4 numbers long, the rest of the code will execute.
        if len(self.generateID) < 4:
            #Generates a random number between 0 and 9 and assigns it to the variable "randomGen"
            randomGen = random.randint(0, 9)
            #Appends the randomly generated ID to the geenrateID string.
            self.generateID = self.generateID + str(randomGen)
            #This is repeated until the length of the ID is 4.
            self.generateID = self.recursionGenerateID(self.generateID)
        return self.generateID

    #detailsValidator method is run when the user presses the "Register" button.
    def detailsValidator(self):
        #The user input length is worked out, in this case for the firstname.
        firstnameLength = len(self.editFirstname.text()) >= 3
        #The user input length is worked out, in this case for the surname.
        surnameLength = len(self.editSurname.text()) >= 3
        #The user input length is worked out, in this case for the email.
        emailLength = len(self.editEmail.text()) >= 12
        #The user input length is worked out, in this case for the mobile number.
        mobileNumberLength = len(self.editMobileNumber.text()) >= 11
        #The user input length is worked out, in this case for the password.
        passwordLength = len(self.editPassword.text()) >= 8

        #Using sets from the regular expressions re module, I am checking if certain characters are in the,
        #user input, in this case in the first name. It's checking if it contains the english,
        #alphabet. It would be false if it contains for example numbers and if it meets the requirements, it will
        #stay True.
        firstnameCharCheck = re.search(r"[a-zA-Z]", self.editFirstname.text()) is None
        surnameCharCheck = re.search(r"[a-zA-Z]", self.editSurname.text()) is None
        emailCharCheck = re.search(r"[a-zA-Z]", self.editEmail.text()) is None
        passwordCharCheck = re.search(r"[a-zA-Z]", self.editPassword.text()) is None

        #Using regular expressions to check if the email inputted by the user has a "@" symbol,
        #and to check that it only appears once.       
        emailSymbolCheck = re.search("@{1}", self.editEmail.text()) is None

        #Using rRegEx, it checks on the user input field for mobile number, there is only,
        #digits/ number entered.
        mobileNumberCheck = re.search(r"\d", self.editMobileNumber.text()) is None
        #Using RegEx, checks to see if the password conatains digits/ numbers.
        passwordNumberCheck = re.search(r"\d", self.editPassword.text()) is None

        passwordSpecialSymbolsCheck = re.search(r"[!, £, $, %, ^, &, *, (, ), -, =, +, @]", self.editPassword.text()) is None
        
        #Executes the "validateRegister" method, passing in 13 paramater checks.
        self.validateRegister(firstnameLength, surnameLength, emailLength,
            firstnameCharCheck, surnameCharCheck, emailCharCheck, emailSymbolCheck, 
            passwordLength, passwordCharCheck, passwordSpecialSymbolsCheck, 
            passwordNumberCheck, mobileNumberCheck, mobileNumberLength)
    
    #"validateRegister" method is executed after the user input checks have been made and the result is taken in,
    #and saved as a boolean value. It recieves 13 variables containing boolean values as arguements.
    def validateRegister(self, firstnameLength, surnameLength, emailLength,
            firstnameCharCheck, surnameCharCheck, emailCharCheck, emailSymbolCheck, 
            passwordLength, passwordCharCheck, passwordSpecialSymbolsCheck, 
            passwordNumberCheck, mobileNumberCheck, mobileNumberLength):

        #Generates a 4 digit unqiue Member ID using a "recursionGenerateID" method.
        inputRandomNum = random.randint(0, 9)
        #A random generated that is stored in the "inputRandomNum" is passed in as a parameter
        #into the "recursionGenerateID" method.
        self.recursionGenerateID(inputRandomNum)

        #Checks for the user input checks.
        #In this case using an if statement checks if the first name is at least 3 characters long.
        #If the firstnameLength is False, it's less than 3 characters long, as from the "detailsValidator",
        #it only turns True if it doesn't meet the length requirements.
        if firstnameLength == False:
            #sendError variable contains the suitable error to be passed onto the showPopupDetailsIncorrect,
            #method as a paramater.
            sendError = "Your firstname should be at least 3 characters long."
            sendErrorDetail = ""
            #showPopupDetailsIncorrect method takes in 2 parameters.
            #shoPopupDetailsIncorrect method is run, if the user input fields, doesn't meet the,
            #requirement and a suitable pop up notification is shown to the user.
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        #Then checks if the first name characters only contains english alphabet.
        elif firstnameCharCheck == True:
            sendError = "Your firstname should contain only the english alphabet."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        
        #Checks for the surname length.
        elif surnameLength == False:
            sendError = "Your surname should be at least 3 characters long."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        #Checks if the surname only contains english alphabet.
        elif surnameCharCheck == True:
            sendError = "Your surname should contain only the english alphabet."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        
        #Checks for the email length.
        elif emailLength == False:
            sendError = "Your email address should be at least 12 characters long."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        #Checks if the email contains only english alphabet.
        elif emailCharCheck == True:
            sendError = "Your email should contain the english alphabet."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        #Checks the email to see if it contains the "@" symbol.
        elif emailSymbolCheck == True:
            sendError = "Your email should contain @."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)

        #Checks for the surname length.
        elif mobileNumberLength == False:
            sendError = "Your mobile number should be at least 11 digits."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        #Checks to see if the mobile number only contains numbers/ digits.
        elif mobileNumberCheck == True:
            sendError = "Your mobile number should only be digits."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        
        #Checks to validate the password meets the required length.
        elif passwordLength == False:
            sendError = "Your password should be at least 8 characters long."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        #Checks to see if the password contains only the english alphabet.
        elif passwordCharCheck == True:
            sendError = "Your password should contain the english alphabet."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        #Checks to see if the password contain digits/ numbers.
        elif passwordNumberCheck == True:
            sendError = "Your password should contain at least 1 digit."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        #Checks to see if the password contains the special characters that it needs to have.
        elif passwordSpecialSymbolsCheck == True:
            sendError = "Your password should contain the 1 of the following special characters !, £, $, %, ^, &, *, (, ), -, =, + or @."
            sendErrorDetail = ""
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)

        #If all the above requirements are met, the else statement will be run.
        else:
            #Hashing
            inputPassword = self.editPassword.text()
            #Converts the text to binary(bytes).
            passwordEncode = inputPassword.encode()
            print("Encoded:", passwordEncode)

            #Add 64  characters of salt to the password before hashing.
            addSalt = os.urandom(32)
            #Converts the binary(bytes) into hex so easily readable and saves space in the database. 
            saltHex = addSalt.hex()
            print("Salt(hex):", saltHex)
            #Hashes the salt generated + the password entered by the user.
            hashPassword = hashlib.pbkdf2_hmac("sha256", passwordEncode, addSalt, 100000)
            #Converts the binary(bytes) into hex so easily readable and saves space in the database. 
            hashPasswordHex = hashPassword.hex()
            print("Hashed password(hex):", hashPasswordHex)

            database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
            connection = CreateConnection(database)
 
            #"with connection" closes the database connection automatically, once the SQL operations are completed.
            with connection:
                member = (self.generateID, self.editFirstname.text().capitalize().strip(), self.editSurname.text().capitalize().strip(), 
                          self.editEmail.text().strip(), self.editMobileNumber.text().strip(), hashPasswordHex, saltHex)
                
                #The new member who have registered is inserted into the Member table in the database.
                InsertMember(connection, member)
                #showPopupDetailsCorrect method is run to notify the user with a pop up message,
                #to inform that they have successfully registered with Qjet as a member.
                self.showPopupDetailsCorrect()
      
    #showPopupDetailsCorrect is run once the user has successfully registered.     
    def showPopupDetailsCorrect(self):  
        message = QMessageBox()
        #Sets the pop up window title to "Successful".
        message.setWindowTitle("Successful")
        #Sets the main information text on the pop up to "You have registered."
        message.setText("You have registered.")
        #This sets the icon of the pop up to a information symbol.
        message.setIcon(QMessageBox.Information)
        #There will be a button for the staff which they can click, and it will expand the pop up
        #to give more detail of the message.
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        #The pop up is executed.
        x = message.exec_()
        
        #The user input fiels will be reseted to blank empty user input boxes, once the user has,
        #sucessfully registered.
        self.editFirstname.setText("")
        self.editSurname.setText("")
        self.editEmail.setText("")
        self.editMobileNumber.setText("")
        self.editPassword.setText("")

    #showPopupDetailsIncorrect is run with it recieving "sendInfo" and "sendErrorDetail" as two arguements.
    #This method is run to inform the user with a pop up with any errors. 
    def showPopupDetailsIncorrect(self, sendError, sendErrorDetail):
        message = QMessageBox()
        message.setWindowTitle("Unsuccessful")
        message.setText(sendError)
        message.setIcon(QMessageBox.Warning)
        message.setDetailedText(sendErrorDetail)

        message.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        x = message.exec_()

    #When the user presses the "back" button, the switchWindowLogin method is run and the register window
    #will be closed. 
    def switchWindowLogin(self, registerWindow):
        registerWindow.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    registerWindow = QtWidgets.QMainWindow()
    gui = showRegisterWindow()
    gui.setupGuiRegister(registerWindow)
    registerWindow.show()
    sys.exit(app.exec_())
        




        
        
    
        
