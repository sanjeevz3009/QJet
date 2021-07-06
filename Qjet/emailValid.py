#Importing the necessary modules.
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

#Imports the system module.
import sys

#Imports the other python files as modules.
#Imports the database file.
from qjetdatabase import *
#Imports the login window.
from loginWindow import *

#Imports the necessary SMTP modules.
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#Imports the random module which helps to random generate numbers.
import random 
import string
#Imports the OS module, so it can be used to generate a arbitary characters
#for my salt which is uniquely generated for each new password entered.
import os 
#Imports hashlib module to help me with hashing the password.
import hashlib

#showEmailWindow class is initated which inherits from QtWidget(QtWidgets.QWidget).
class showEmailWindow(QtWidgets.QWidget):
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
    
    def setupGuiEmail(self, emailWindow):
        #Setting the window title.
        emailWindow.setWindowTitle("Password - reset page")
        emailWindow.resize(900, 700)
        #Restricting the resize minimum and maximum window size to 900 by 700.
        emailWindow.setMinimumSize(QtCore.QSize(900, 700))
        emailWindow.setMaximumSize(QtCore.QSize(900, 700))
        
        #Setting up the QJet logo for the log in window icon. 
        icon = QtGui.QIcon()
        #Imports the qjetLogo.png from the current folders it's in and display it on the login window.
        icon.addPixmap(QtGui.QPixmap("qjetLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        emailWindow.setWindowIcon(icon)
        
        #Positions the forgot password title to the center of the member window.
        self.centralwidget = QtWidgets.QWidget(emailWindow)
        
        #Creates the title for forgot password window.
        self.title = QtWidgets.QLabel(self.centralwidget)
        #Sets the forgot password window title to the specified title.
        self.title.setText("Password reset page")
        #Positions the Qjet title in the member window.
        self.title.setGeometry(QtCore.QRect(260, 0, 371, 81))
        
        #Sets up the font style, underlines and font size for the forgot password window title.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        #Designs the forgot password title using all the QFont methods above.
        self.title.setFont(font)

        #Sets up the background image.
        self.background = QtWidgets.QLabel(self.centralwidget)
        #Positions the backgreound image.
        self.background.setGeometry(QtCore.QRect(0, 0, 901, 700))
        self.background.setText("")
        #Imports the aviation.png from the current folders it's in.
        self.background.setPixmap(QtGui.QPixmap("aviation.png"))
        #Makes the image less blurry by importing and placing it to scale.
        self.background.setScaledContents(True)
        self.background.setWordWrap(False)

        #Brings the title front over the background.
        self.title.raise_()
        
        #Creates the logo box to display the logo in the forgot password window.
        self.logo = QtWidgets.QLabel(self.centralwidget)
        #Sets the position of the logo and size(dimension).
        self.logo.setGeometry(QtCore.QRect(10, 60, 171, 181))
        #Sets the logo text to NONE as there will not be a need to have a custom text over the logo.
        self.logo.setText("")
        #Gets the qjetLogo.png from the current directory and sets it as the logo.
        self.logo.setPixmap(QtGui.QPixmap("qjetLogo.png"))
        #Scales the logo(content), so the logo isn't blurry.
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        
        #Creates the email text on the forgot password window.
        self.labelEmail = QtWidgets.QLabel(self.centralwidget)
        #Sets the email title to the specified text.
        self.labelEmail.setText("Enter your email:")
        #Positions and sets the dimensions (positions and size) of the email text.
        self.labelEmail.setGeometry(QtCore.QRect(10, 270, 301, 81))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        self.labelEmail.setFont(font)
        
        #Creates the user input box for the email to be entered.
        self.editEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.editEmail.setGeometry(QtCore.QRect(320, 280, 441, 61))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        
        self.editEmail.setFont(font)
        
        #Creates the back button on the forgot password window.
        self.buttonBack = QtWidgets.QPushButton(self.centralwidget)
        #Sets the text to the specified text for the back button.
        self.buttonBack.setText("Back")
        self.buttonBack.setGeometry(QtCore.QRect(10, 360, 291, 71))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.buttonBack.setFont(font)
        
        #When the back button is clicked the switchWindowLogin method is run and forgot password window will
        #be closed.
        #A lambda function is a small anonymous function and in this case used to pass emailWindow
        #(that contains thw forgot password window) window class to switchWindowLogin to close the forgot password window.
        self.buttonBack.clicked.connect(lambda:self.switchWindowLogin(emailWindow))
        
        #Creates the submit button.
        self.buttonSubmit = QtWidgets.QPushButton(self.centralwidget)
        #Sets the text to the specified text for the submit button
        self.buttonSubmit.setText("Submit")
        self.buttonSubmit.setGeometry(QtCore.QRect(450, 360, 311, 71))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.buttonSubmit.setFont(font)
        
        #When the user pressed the "Submit" button, the "validate" method is run.
        self.buttonSubmit.clicked.connect(self.validate)
        
        emailWindow.setCentralWidget(self.centralwidget)

    #Validates if the the user has entered their email and it's correct
    #and then the a password is generated and the hash and salt is stored in te database.
    #The raw plain English password is sent to the user's email.
    def validate(self):
        #If the user input (email) is empty, the error is catched and outputted.
        if self.editEmail.text() == "":
            print("Enter something!")
        else:
            #If the email is entered the rest of the code will continue to run.
            pass
        sendEmail = self.editEmail.text()

        #Specifies the location of the database.
        database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
        #Creates the database connection.
        connection = CreateConnection(database)
        with connection:
            #Hashing
            #Calls the passwordGenerate method to generate a 10 character password.
            #Passes the number 10, to generate a 10 characters.
            inputPassword = self.passwordGenerate(10)
            #Converts the text to binary(bytes).
            passwordEncode = inputPassword.encode()
            print("Encoded:", passwordEncode)

            #Add 64 hex characters of salt to the to the hex of the password before hashing.
            addSalt = os.urandom(32)
            #Converts the binary(bytes) into hex so easily readable and saves space in the database. 
            saltHex = addSalt.hex()
            print("Salt(hex):", saltHex)
            #Hashes the salt generated + the password entered by the user.
            hashPassword = hashlib.pbkdf2_hmac("sha256", passwordEncode, addSalt, 100000)
            #Converts the binary(bytes) into hex so easily readable and saves space in the database. 
            hashPasswordHex = hashPassword.hex()
            print("Hashed password(hex):", hashPasswordHex)

        #The generate password which is generated using the passworsGenerate method is stored
        #in the inputPassword variable.
        sendPassword = inputPassword

        #Instantiates the emailSender() class.
        a = emaileSender()
        #The sendCode() method is executed, with being passed 4 parameters.
        a.sendCode(sendEmail, sendPassword, hashPasswordHex, saltHex)

    #Password generate alogrithm. It generates a password with length of 10 characters.
    def passwordGenerate(self, length, characters=string.ascii_letters + string.digits):
        return ''.join(random.choice(characters) for i in range(length))
    
    #When the password is succesfully sent to the user's email, a pop up notification
    #is displayed to the user. showPopupDetailsCorrect will be executed, when the password
    #is successfully generated and stored in the database.
    def showPopupDetailsCorrect(self):
        message = QMessageBox()
        message.setWindowTitle("Successful")
        message.setText("Your passsword has been sent to your email.")
        message.setIcon(QMessageBox.Information)

        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        x = message.exec_()
        self.lineEditEmail.setText("")
    
    #If the user doesn't enter their email, email not in the right format or if it's an invalid email
    #this error pop up notification will be displayed to the user.
    #showPopupDetailsIncorrect method will be executed.
    def showPopupDetailsIncorrect(self):
        message = QMessageBox()
        message.setWindowTitle("Unsuccessful.")
        message.setText("You have entered a invalid email.")
        message.setIcon(QMessageBox.Information)
    
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        x = message.exec_()
        self.lineEditEmail.setText("")
    
    #When the user clicks the "Back" button, the forgot password window/ page will be closed,
    #and the user will be taken back to the login page.
    #switchWindowLogin method will be executed recieving "emailWindow" as an arguement from a lambda function.
    def switchWindowLogin(self, emailWindow):
        #The forgot password window will be closed and the user will be taken to the login window.
        emailWindow.close() 

#This class performs certain operations that is needed to send the booked flights tickets of a member to their email.
#This emailSenderTickets class inherits from the showEmailWindow class.
class emailSenderTickets(showEmailWindow):
    def __init__(self, sendMemberID):
        #When you add the __init__() function, the child class will no longer inherit,
        #The parent's __init__() function.
        #The child's __init__() function overrides the inheritance of the parent's __init__() function.
        #Child class that inherits the properties and methods from its parent.
        self.sendMemberID = sendMemberID

    #sendTickets method is executed, when the member in the member window/ page presses the,
    #"Send tickets" button. This method is used to send the booked flights ticket of a member to their email.
    def sendTickets(self):
        #Specifies the location of the database.
        database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
        #Creates the database connection.
        connection = CreateConnection(database)
        #Creates the cursor object by calling the cursor() function method of the connection object.
        c = connection.cursor()

        #Executes a SQL statement to retrieve Email from the Member table.
        c.execute("SELECT Email FROM Member WHERE MemberID = ?", [self.sendMemberID])
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        details = []
        #Gets the data from the database as arrays and performs a list comprehension and stores the email addresses in a list.
        for i in data:
            for j in i:
                #Appends the email to the details list.
                details.append(j)

        #Gets the member email by using the index position 0 as this will be the member's email address in the list.
        email = details[0]
        print(email)

        #A try except block is run to get flight ID of the flights that the member booked, and
        #the the flight names and prices. Finally emailing all these details to the member's email.
        try:
            database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
            connection = CreateConnection(database)
            c = connection.cursor()
            #Executes a SQL statement to retrieve FlightID from the FlightsBooked table, using the memberID.
            c.execute("SELECT FlightID FROM FlightsBooked WHERE MemberID = ?", [self.sendMemberID])
            #Calls the fetchall() method of the cursor object to fetch the data.
            data = c.fetchall()

            flightIDs = []

            #A list comprehension is performed to convert the items from 2D array to a 1D list.
            for flightID in data:
                for flightIDList in flightID:
                    #The flight ID is appended to the "flightIDs" 1D list.
                    flightIDs.append(flightIDList)
            print(flightIDs)

        #If the query failed to get the FlightID using the FlightName, the self.dataBook will not be 
        #intialised, thus an attriut error will be thrown in the program. I can catch the error using
        #this except AttributeError block.
        except AttributeError as error:
            print(error)

        flightNames = []

        for i in range(len(flightIDs)):
            #Executes a SQL statement to retrieve flight name from the Flights table, using the FlightID.
            c.execute("SELECT FlightName FROM Flights WHERE FlightID = ?", [flightIDs[i]])
            #Calls the fetchall() method of the cursor object to fetch the data.
            data = c.fetchall()

            #Loops through all the flight names in the data array and a list comprehension is performed.
            for flightName in data:
                for flightNameList in flightName:
                    #All the flight names are appended to the flightNames 1D list.
                    flightNames.append(flightNameList)
            print(flightNames)

        #A string variable is created.
        flightNamesText = ""
        #Until the length of the lnegth of the flightNames list the for loop is run.
        for i in range (len(flightNames)):
            #The flight names are appended to the string variable flightNamesText
            flightNamesText += "*" + flightNames[i] + "\n" + "\n"

        #User's is overriden to the variable userInput to be used later.
        userInput = email
        subject = "Your flight tickets:"
        recieveTickets = "Your flight tickets: " + "\n" + "=============="+ "\n" + flightNamesText

        #SMTP server username.
        username = "qjetbot1111@gmail.com"
        #SMTP server password.
        password = "Qjet1010"
        message = MIMEMultipart("mixed")
        
        #Subject for the email.
        message["Subject"] = subject
        #Message for the email.
        message["From"] = username
        #The email address to send the email.
        message["To"] = userInput

        #Text to send in the email, in this case the password for the email address requested to be resetted.
        textMessage = MIMEText(recieveTickets, "plain")
        #htmlMessage = MIMEText(, "html")
        #Attaches the message
        message.attach(textMessage)
        #message.attach(htmlMessage)

        #Connects to the gmail server, in this case using gmail SMTP server and using port 587.
        mailServer = smtplib.SMTP("smtp.gmail.com", 587) #Alternative ports: 8025, 587 and 25.
        #Identify yourself to an ESMTP server using EHLO.
        mailServer.ehlo()
        #Puts the SMTP connection in TLS(Transport Layer Security) mode.
        #All SMTP commands that follow will be encrypted.
        mailServer.starttls()
        mailServer.ehlo()
        #Logins to the gmail server using the username and password provided.
        mailServer.login(username, password)
        #Sends the email to the email address with it's content.
        mailServer.sendmail(userInput, userInput, message.as_string())
        #Closes the mail server.
        mailServer.close()

        print(f"Your flight tickets has been sent to {userInput}.")

class emailSender(object):
    #Constructor is made, __init__() function to assign values to object properties or
    #other operations that are necessaeay to do when the objects is being created.
    #The __init__() function is called automatically every time the class is 
    #being used to create a new object.

    #This constructor recieves sendAdminID as a paramater from the
    #login window(loginWindow).
    #The self parameter is a reference to the current instance of the class,
    #and is used to access variables that belong to the class.
    def __init__(self):
        pass

    #sendCode method Recieves the email and password as agruements from the password reset window. 
    #This method is used to reset/ generate new password for the member and send the password to the,
    #member's email.
    def sendCode(self, email, password, hashPasswordHex, saltHex):
        database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
        connection = CreateConnection(database)
        c = connection.cursor()

        #with connection closes the database connection automatically, once the operations,
        #are completed.
        with connection:
            #SQL statement is assigned to the variable sql.
            #This SQL statement contains the code to UPDATE the member hash and salt which makes up the,
            #overall password.
            sql = """UPDATE Member SET Hash = ?, Salt = ? WHERE Email = ?"""
            #Using my qjetdatabase module, memberUpdate function is used to update the member's hash and salt,
            #(password).
            memberUpdate = (hashPasswordHex, saltHex, email)
            #The update is executed and the hash and salt (password) of the member will be updated. 
            c.execute(sql, memberUpdate)

        #User's is overriden to the variable userInput to be used later.
        userInput = email
        subject = "Password reset:"
        recievePassword = "Your password is: " + password

        #SMTP server username.
        username = "qjetbot1111@gmail.com"
        #SMTP server password.
        password = "Qjet1010"
        message = MIMEMultipart("mixed")
        
        #Subject for the email.
        message["Subject"] = subject
        #Message for the email.
        message["From"] = username
        #The email address to send the email.
        message["To"] = userInput

        #Text to send in the email, in this case the password for the email address requested to be resetted.
        textMessage = MIMEText(recievePassword, "plain")
        #htmlMessage = MIMEText(, "html")
        #Attaches the message
        message.attach(textMessage)
        #message.attach(htmlMessage)

        #Connects to the gmail server, in this case uisng gmail SMTP server and using port 587.
        mailServer = smtplib.SMTP("smtp.gmail.com", 587) #Alternative ports: 8025, 587 and 25.
        #Identify yourself to an ESMTP server using EHLO.
        mailServer.ehlo()
        #Puts the SMTP connection in TLS(Transport Layer Security) mode.
        #All SMTP commands that follow will be encrypted.
        mailServer.starttls()
        mailServer.ehlo()
        #Logins to the gmail server using the username and password provided.
        mailServer.login(username, password)
        #Sends the email to the email address with it's content.
        #Try except block is run to send the email.
        try:
            mailServer.sendmail(userInput, userInput, message.as_string())
            #Closes the mail server.
            mailServer.close()
            print(f"Your password has been sent to {userInput}.")
            self.showPopupDetailsCorrect()
        except:
            print("Invalid email address.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    emailWindow = QtWidgets.QMainWindow()
    gui = showEmailWindow()
    gui.setupGuiEmail(emailWindow)
    emailWindow.show()
    sys.exit(app.exec_())
