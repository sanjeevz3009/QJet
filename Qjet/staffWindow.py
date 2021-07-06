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
#Imports the login window.
from loginWindow import *
#Imports the random module.
from random import *

#Imports the hashlib module, which is used to help me hash the password.
import hashlib
#Imports the OS module, so it can be used to generate a arbitary charatcers
#for my salt which is uniquely generated for each new password entered.
import os

#showStaffWindow class is initiated which inherits from QtWidget(QtWidgets.QWidget).
class showStaffWindow(QtWidgets.QWidget):
    #Constructor is made, __init__() function to assign values to object properties or
    #other operations that are necessaeay to do when the objects is being created.
    #The __init__() function is called automatically every time the class is 
    #being used to create a new object.

    #This constructor recieves sendAdminID as a paramater from the
    #login window(loginWindow).
    #The self parameter is a reference to the current instance of the class,
    #and is used to access variables that belong to the class.
    def __init__(self, sendStaffID):
        #super() function that will make the child class inherit all the methods and properties from its parent.
        super().__init__()   
        #The self parameter is a reference to the current instance of the class,
        #and is used to access variables that belongs to the class.    
        self.sendStaffID = sendStaffID
    
    #Objects can also contain methods. Methods in objects are functions that belong to the object.
    def setupGuiStaff(self, staffWindow):
        #Database local location is assigned to the variable database.
        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"

        #Executes a sql statement to retrieve FirstName, Surname, Email, MobileNumber and Password.
        #from the staff table.
        connection = CreateConnection(database)
        c = connection.cursor()
        c.execute("SELECT FirstName, Surname, Email, MobileNumber FROM Staff WHERE StaffID = ?", [self.sendStaffID])
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a details list, so details can be appended after a list comprehension is performed
        #on the data retrieved as arrays. It will have FirstName, Surname, Email, MobileNumber and Password data.
        details = []

        #Gets the data from the database as arrays and performs a list comprehension and stores staff id in a list.
        #A nested for loop is run for this operation.
        for detail in data:
            for detailList in detail:
                details.append(detailList)
        print(details)

        #Assigns the correct items from the list to the correct variable names.
        firstName = details[0]
        surname = details[1]
        email = details[2]
        mobileNumber = details[3]
        
        #Setting the window title.
        staffWindow.setWindowTitle("Staff page")
        staffWindow.resize(900, 700)
        #Restricting the resize minimum and maximum window size to 900 by 700.
        staffWindow.setMinimumSize(QtCore.QSize(900, 700))
        staffWindow.setMaximumSize(QtCore.QSize(900, 700))
        
        #Setting up the QJet logo for the log in window icon. 
        icon = QtGui.QIcon()
        #Imports the qjetLogo.png from the current folders it's in and display it on the login window.
        icon.addPixmap(QtGui.QPixmap("qjetLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        staffWindow.setWindowIcon(icon)
        
        #Positions the staff title to the center of the staff window.
        self.centralwidget = QtWidgets.QWidget(staffWindow)
        
        #Creates the title in the staff window.
        self.title = QtWidgets.QLabel(self.centralwidget)
        #Positions the Qjet title in the staff window.
        self.title.setGeometry(QtCore.QRect(370, -10, 181, 81))
        #Sets the title text.
        self.title.setText("Staff page")

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
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        #Sets the staff window title to the specified title.
        self.title.setFont(font)

        #Sets up the Welcome text which will say "Welcome FIRSTNAME SURNAME"
        self.titleWelcome = QtWidgets.QLabel(self.centralwidget)
        #Positions the welcome text.
        self.titleWelcome.setGeometry(QtCore.QRect(10, 50, 250, 40))

        self.title.setText("Staff page")
        
        #Sets up the font style, underlines and font size for the staff welcome text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        #Designs the staff window welcome text using all the QFont methods above.
        self.titleWelcome.setFont(font)
        #Sets the text and adds the variable name firstName and surname which has the firstname and surname values
        #which was retrieved from querying the database.
        self.titleWelcome.setText("Welcome, " + firstName + " " + surname)
        #Designs the welcome text with colour, border, size and padding.
        self.titleWelcome.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: green;
    font: bold 14px;
    min-width: 10em;
    padding: 5px;""")
        
        #Creates the logout button.
        self.buttonLogOut = QtWidgets.QPushButton(self.centralwidget)
        #Positions the logout button and sets the size(dimensions).
        self.buttonLogOut.setGeometry(QtCore.QRect(10, 600, 101, 41))
        
        #Sets up the font style, underlines and font size for the log out button.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        #Designs the staff window Logout button text using all the QFont methods above.
        self.buttonLogOut.setFont(font)
        #Creates an blue outline for the log out button which glows when hovered over.
        self.buttonLogOut.setDefault(True)
        #Sets the button text.
        self.buttonLogOut.setText("Logout")
        
        #When the login button is clicked the switchStaffWindow method is run and staff window will
        #be closed.
        #A lambda function is a small anonymous function and in this case used to pass staff window class
        #to switchStaffWindow to close the staff window.
        self.buttonLogOut.clicked.connect(lambda:self.switchWindowStaff(staffWindow))
        
        #Creates a text label called "My personal details:" in the staff window.
        self.titlePersonalDetails = QtWidgets.QLabel(self.centralwidget)
        #Sets the dimesions (size and positions) in the staff window.
        self.titlePersonalDetails.setGeometry(QtCore.QRect(180, 155, 180, 40))
        
        #Sets up the font style, underlines and font size for the text that says "My personal details:".
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        #Designs the staff window "My personal details:" text using all the QFont methods above.
        self.titlePersonalDetails.setFont(font)
        self.titlePersonalDetails.setText("My personal details:")
        #Designs the "My persona details:" text with colour, border, size and padding.
        self.titlePersonalDetails.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: red;
    font: bold 13px;
    min-width: 2em;
    padding: 10px;""")

        #Creates the box that contains the labels/ text of firstname, surname, email, mobile number
        #and password text.
        self.textEditDetails = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditDetails.setEnabled(False)
        #Positions the the box of text and sets the size(dimensions).
        self.textEditDetails.setGeometry(QtCore.QRect(10, 180, 131, 191))
        self.textEditDetails.setPlainText("My details:\n"
"\n"
"Firstname:\n"
"\n"
"Surname:\n"
"\n"
"Email:\n"
"\n"
"Mobile number:\n"
"\n"
"Password:")
        self.textEditDetails.setUndoRedoEnabled(False)
        #Designs the boxes that contains the names that specify firstname, surname, email, 
        #mobile number and password.
        #Designs the text to black text colour and background of the text or the box to light
        #blue colour.
        self.textEditDetails.setStyleSheet("background-color: #2094ed; color: black")

        #Creates the user input box that contains the firstname which is not editable.
        #Unless alter/change details button is clicked, where the box will be unfroze
        #so the user can edit the details and click the save details button to save 
        #the new details to the database.
        self.editFirstname = QtWidgets.QLineEdit(self.centralwidget)
        #The input box is froze so the user cannot accidently change the details
        #unless the users intentionally wants to in that case the user can which 
        #a click of a button underneath the box.
        self.editFirstname.setEnabled(False)
        #Positions the the user input box of text and sets the size(dimensions).
        self.editFirstname.setGeometry(QtCore.QRect(140, 200, 281, 31))
        #Sets the text inside the text box from the queried details from the database.
        self.editFirstname.setText(firstName)
        #Designs the input box with the text colour being black.
        self.editFirstname.setStyleSheet("color: black")
        
        #Creates the surname usewr input box.
        self.editSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.editSurname.setEnabled(False)
        self.editSurname.setGeometry(QtCore.QRect(140, 230, 281, 31))
        self.editSurname.setText(surname)
        self.editSurname.setStyleSheet("color: black")
        
        #Creates the email user input box.
        self.editEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.editEmail.setEnabled(False)
        self.editEmail.setGeometry(QtCore.QRect(140, 260, 281, 41))
        self.editEmail.setText(email)
        self.editEmail.setStyleSheet("color: black")

        #Creates the email mobile number user input box.
        self.editMobileNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.editMobileNumber.setEnabled(False)
        self.editMobileNumber.setGeometry(QtCore.QRect(140, 300, 281, 41))
        self.editMobileNumber.setText(str(mobileNumber))
        self.editMobileNumber.setStyleSheet("color: black")
        
        #Creates the alter/ change my details button which us used to unfreeze the input boxes
        #so the user can edit the details and save it, which will be updated to the database.
        self.buttonChangeDetails = QtWidgets.QPushButton(self.centralwidget)
        #Positions the alter/ change my details button and sets the size(dimensions).
        self.buttonChangeDetails.setGeometry(QtCore.QRect(10, 390, 411, 71))
              
        #Sets up the font style, underlines and font size for the button text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        #Designs the staff window button text using all the QFont methods above.
        self.buttonChangeDetails.setFont(font)
        #Creates an blue outline for the log out button which glows when hovered over.
        self.buttonChangeDetails.setDefault(True)
        #When the alter/ change my details button is clicked it goes to the editDetails method.
        #Where the method unfreezes the input boxes and the user will be able to edit their details
        #and then save it which will be updated to the database.
        self.buttonChangeDetails.setText("Alter/ change my details")
        #When the alter/ change my details button is clicked it goes to the editDetails method.
        #Where the method unfreezes the input boxes and the user will be able to edit their details
        #and then save it which will be updated to the database.
        self.buttonChangeDetails.clicked.connect(self.editDetails)
        
        #Creates the password user input box.
        self.editPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.editPassword.setEnabled(False)
        self.editPassword.setGeometry(QtCore.QRect(140, 340, 281, 31))
        self.editPassword.setStyleSheet("color: black")
        #Shows a tooltip(Text popping up showing text) when hovered over the password user input box.
        self.editPassword.setToolTip("<h3>Enter your new password here.<h3>")

        #Creates the logo box to display the logo in the staff window.
        self.logo = QtWidgets.QLabel(self.centralwidget)
        #Sets the position of the logo and size(dimension).
        self.logo.setGeometry(QtCore.QRect(720, 0, 171, 181))
        #Sets the logo text to NONE as there will not be a need to have a custom text over the logo.
        self.logo.setText("")
        #Gets the qjetLogo.png from the current directory and sets it as the logo.
        self.logo.setPixmap(QtGui.QPixmap("qjetLogo.png"))
        #Scales the logo(content), so the logo isn't blurry.
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)

        #Creates the text called "Currently acitve flight routes".
        self.titleCurrentFlights = QtWidgets.QLabel(self.centralwidget)
        #Positions the the text and sets the dimensions (positions and size).
        self.titleCurrentFlights.setGeometry(QtCore.QRect(430, 140, 351, 81))

        #Sets up the font style, underlines and font size for the "Current actively flights"
        #text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        #Designs the "Currently active flight routes" text using all the QFont methods above.
        self.titleCurrentFlights.setFont(font)
        #Sets the text.
        self.titleCurrentFlights.setText("Currently active flight routes")

        #Creates the text called "Select the flight route to cancel/ remove".
        self.titleSelectFlights = QtWidgets.QLabel(self.centralwidget)
        self.titleSelectFlights.setGeometry(QtCore.QRect(430, 370, 471, 41))

        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        self.titleSelectFlights.setFont(font)
        self.titleSelectFlights.setText("Select the flight route to cancel/ remove")

        #Creates the box for, the staff to see the already active or added flights (flight routes).
        self.textEditBook = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditBook.setGeometry(QtCore.QRect(430, 200, 451, 171))
        self.textEditBook.setEnabled(True)
        self.textEditBook.setReadOnly(True)

        #Database local location is assigned to the variable database.
        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"

        #Using the CreateConnection function in my database module, it creates the database connection
        #and assigns it to connection variable.
        connection = CreateConnection(database)
        #Creates the cursor object by calling the cursor() function method of the connection object.
        c = connection.cursor()
        #Executes a SQL statement to retrieve the FlightName from the Flights table.
        c.execute("SELECT FlightName FROM Flights")
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a details list, so details can be appended after a list comprehension is performed
        #on the data retrieved as arrays. It will have flightNames.
        flightNames = []

        #Gets the data from the database as arrays and performs a list comprehension and stores flightName in a list.
        #A nested for loop is run for this operation.
        for flightName in data:
            for flightNameList in flightName:
                flightNames.append(flightNameList)
        print(flightNames)

        #Assigns a empty string to the flightNamesText variable.
        #So a string operation/ manipulation can be performed.
        flightNamesText = ""

        #A for loop is ran for the duration of the length of the flightNames 1D list.
        for i in range (len(flightNames)):
            #String operations performed and each flight name is appended to the flightNamesText string variable.
            flightNamesText += "*" + flightNames[i] + "\n" + "\n"

        #Sets the flightNamesText to the box that was created to display the flight names.
        self.textEditBook.setPlainText(flightNamesText)
        #Sets the text colour to black.
        self.textEditBook.setStyleSheet("color: black")

        #Creates the cancel information text, it explains how to cancel the flights (flight routes).
        self.textEditCancel = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditCancel.setEnabled(False)
        self.textEditCancel.setGeometry(QtCore.QRect(430, 410, 450, 51))
        self.textEditCancel.setPlainText("Select the flight route from the list below and press the cancel button to remove the flight route.")
        self.textEditCancel.setStyleSheet("color: black")

        #Creates the drop down list box that contains the active flights, which the staff can select and
        #can cancel/ remove so the member won't be able to book the flights.
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        #Positions the drop down list box and sets the size(dimensions).
        self.comboBox.setGeometry(QtCore.QRect(430, 470, 350, 31))

        #The default item in the flight cancel drop down list box will be "Please select the flight."
        self.comboBox.addItem("Please select the flight")

        #A for loop is run until the duration of the length of the flightNames list.
        for i in range (len(flightNames)):
            #Each flight name (flight route) is added to the flight cancel drop down list.
            self.comboBox.addItem(flightNames[i])

        #When the staff selects the flights to cancel from the drop down list box, the flight name will be recorded/ captured
        #and sent to the delFlightsData method.
        self.comboBox.activated[str].connect(self.delFlightsData)      

        #Creates the cancel button.
        self.buttonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCancel.setGeometry(QtCore.QRect(785, 470, 95, 31))
        self.buttonCancel.setText("Cancel")
        self.buttonCancel.setStyleSheet("background-color: #2094ed; color: black")
        self.buttonCancel.clicked.connect(self.delFlights)

        #Creates the "Enter the flight route to add flight route" text.
        self.titleSelectFlights2 = QtWidgets.QLabel(self.centralwidget)
        self.titleSelectFlights2.setGeometry(QtCore.QRect(430, 505, 450, 31))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        self.titleSelectFlights2.setFont(font)
        self.titleSelectFlights2.setText("Enter the flight route to add flight route.")
        self.titleSelectFlights2.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: red;
    font: bold 18px;
    min-width: 2em;
    padding: 22px;""")

        #Creates "Enter the flight route below and press add button to add the flight.",
        #text.
        self.textEditAdd = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditAdd.setEnabled(False)
        self.textEditAdd.setGeometry(QtCore.QRect(430, 540, 450, 51))
        self.textEditAdd.setPlainText("Enter the flight route below and press add button to add the flight.")
        self.textEditAdd.setStyleSheet("color: black")
        
        #Creates the user input box for the staff, so they can add new flights (flight routes).
        self.editAddFlights = QtWidgets.QLineEdit(self.centralwidget)
        self.editAddFlights.setGeometry(QtCore.QRect(432, 600, 348, 31))

        #Creates the add button related to add flights user input box.
        #This button will add the new fligh route entered by the staff.
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAdd.setGeometry(QtCore.QRect(785, 600, 95, 31))
        self.buttonAdd.setText("Add")  
        self.buttonAdd.setStyleSheet("background-color: #2094ed; color: black")

        #When the add button is clicked the addFlights method.
        self.buttonAdd.clicked.connect(self.addFlights)

        #Creates the "Help:" text in the staff window.
        self.titleHelp = QtWidgets.QLabel(self.centralwidget)
        self.titleHelp.setGeometry(QtCore.QRect(10, 463, 65, 35))
        
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        self.titleHelp.setFont(font)
        self.titleHelp.setText("Help:")
        self.titleHelp.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: red;
    font: bold 18px;
    min-width: 2em;
    padding: 2px;""")

        #Creates the overiew text in the staff window, which explains briefly what the staff,
        #can do in the staff window.
        self.textEditHelp = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditHelp.setEnabled(False)
        self.textEditHelp.setGeometry(QtCore.QRect(10, 500, 411, 91))
        self.textEditHelp.setPlainText("""-Welcome to Qjet staff page. Here you can add and remove flights.

-You can also alter/ change your presonal details.
-Make sure to save to save your details before you log out.
            """)
        self.textEditHelp.setStyleSheet("color: black")

        staffWindow.setCentralWidget(self.centralwidget)
    
    #editDetails method is ran when the user pressed "Alter/ change my details" button,
    #the editDetails method will be run.       
    def editDetails(self):
        #All the user input boxes will be unfroze, so the staff can input their latest/ new details.
        self.editFirstname.setEnabled(True)
        self.editSurname.setEnabled(True)
        self.editEmail.setEnabled(True)
        self.editMobileNumber.setEnabled(True)
        self.editPassword.setEnabled(True)
        
        #Using polymorphism the button text will be changed from "Alter/ change my details" to "Save details" in real time,
        #in the program.
        self.buttonChangeDetails.setText("Save details")
        
        #When the button is clicked again, to save to details, the saveDetails method will be run.
        self.buttonChangeDetails.clicked.connect(self.saveDetails)
    
    #saveDetails method is run to update the staff details.
    def saveDetails(self):
        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
        connection = CreateConnection(database)

        #Only if the password is more than 8 characters long, the rest of the code will be executed.
        if len(self.editPassword.text()) < 8:
            #showPopupDetailsIncorrect method will be run with one paramater being passed in.
            #This pops up a notification pop up to the staff.
            self.showPopupDetailsIncorrect("Password has to be more than 8 characters.")
        else:
            with connection:
                #Hashing
                inputPassword = self.editPassword.text()
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

                #The updateStaff function will be run from my qjetdatabase module I have imported.
                updateStaff(connection, (self.editFirstname.text(), self.editSurname.text(), 
                            self.editEmail.text(), self.editMobileNumber.text(), hashPasswordHex, saltHex, self.sendStaffID))
                
                #The user input boxes will freeze again, which will make it not possible for accidental changed to the,
                #staff details.
                self.editFirstname.setEnabled(False)
                self.editSurname.setEnabled(False)
                self.editEmail.setEnabled(False)
                self.editMobileNumber.setEnabled(False)
                self.editPassword.setEnabled(False)
                
                #The button text will be changed back to "Alter/ change my details" from "Save details".
                #This is a form of polymorphism.
                self.buttonChangeDetails.setText("Alter/ change my details")
                #If the staff wishes to change the details again, the editDetails method will be run again.
                self.buttonChangeDetails.clicked.connect(self.editDetails)

    #addFlights method is run, when the staff wants to add a new flight (flight route) and,
    #the staff enters the flight name and pressed the "Add" button in the staff window/ page.
    def addFlights(self):
        #Generates a 4 digit unqiue flight ID using a efficient algorithm.
        rangeStart = 10**(4 - 1)
        rangeEnd = (10**4) - 1
        generate = randint(rangeStart, rangeEnd)

        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
        connection = CreateConnection(database)

        #If the add flight user input box is empty, a suitable pop up notification will be executed.
        if self.editAddFlights.text() == "":
            #showPopupDetailsCorrect method is executed, with the text "Enter the flight route." being
            #passed as a paramater.
            self.showPopupDetailsCorrect("Enter the flight route.")
        #Else block is run, if the staff enters the flight route.
        else:
            #Try except block is run to add the new flight route entered by the staff to insert into the database,
            #and to add the new flight route to the active flight route display box in real time.
            try:
                #"with connection" is used so the connection of the database closes automatically.
                #Preventing the database from not saving or being open.
                with connection:
                    #First the new flight route entered by staff is added to the cancel flights,
                    #drop down list box instantly.
                    self.comboBox.addItem(self.editAddFlights.text())

                    #The flight route is also inserted into the Flights table in the database.
                    #flight variable contains which takes in two further variables, one is the
                    #uniquely generated 4 digit flight ID number and the other is the new flight route,
                    #that the staff has inputted.
                    flight = (generate, self.editAddFlights.text())
                    #Using my qjetdatabase module, I can the "InsertFlights" function and pass in 2 parameters,
                    #and the new flight route inputted by the user will be added to the Flights table in the,
                    #database.
                    InsertFlights(connection, flight)
                    #showPopupDetailsCorrect method is run with "Flight route successfuly added." text being,
                    #passed in as paramaters.
                    self.showPopupDetailsCorrect("Flight route successfully added.")

                    c = connection.cursor()
                    #This SQL query is executed to get the FlightNames of the flights in the Flights table,
                    #in the database. So it can be updated real time to the active flights to the active flights,
                    #display box for the staff.
                    c.execute("SELECT FlightName FROM Flights")
                    data = c.fetchall()

                    flightNames = []

                    #A list comprehension is performed to convert the 2D array/ list to 1D list.
                    for flightName in data:
                        for flightNameList in flightName:
                            #Each of the flight names will be appended to the flightNames list.
                            flightNames.append(flightNameList)
                    print(flightNames)

                    #The staff active flights display box will be reseted to blank empty box.
                    self.textEditFlights.setPlainText("")

                    flightNamesText = ""

                    #A for loop is run, so a string operation can be performd for each flight name in the,
                    #flightNames list can be appended to the flightNamesText string variable.
                    for i in range (len(flightNames)):
                        flightNamesText += "*" + flightNames[i] + "\n" + "\n"
                    #The appended flight names will be inputted to the active flights display box in the staff window.
                    self.textEditFlights.setPlainText(flightNamesText)
                    #The text colour is set to black.
                    self.textEditFlights.setStyleSheet("color: black")

            #If there was an error with the SQL queries the error will be catched and printed out to the console,
            #so later it can be fixed.
            #This doesn't crash the program.
            except Error as e:
                print(e)
    
    #delFlightsData method is run when the staff selects a fight to cancel/ delete from the cancel flight,
    #drop down list box. 
    #This will execute the delFlightsData method to run and it will recieve "text" variable as an arguement.
    def delFlightsData(self, text):
        #"self.data" instance variable is created and it takes in the "text" variable as the attribute which contains,
        #the the flight the staff selected to cancel/ remove.
        self.data = text 
        print(self.data)
    
    #When the "Cancel" button is pressed delFlights method will execute.
    def delFlights(self):
        
        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
        connection = CreateConnection(database)
        c = connection.cursor()

        #Try and except block is run to get the FlightID from the Flights table using the FlightName that the Staff,
        #selected.
        try:
            #Execute the SQL query.
            c.execute("SELECT FlightID FROM Flights WHERE FlightName = ?", [self.data])
            #Any Attribute error is catched, such as "self.data" has no data assigned to it.
            #the error will be catched without crashing the program.
        except AttributeError as error:
            print(error)
            #showPopupDetailCorrect method will be run, notifying the staff with a pop up.
            #This method taked one paramater with is a text message called "Flights not selected.".
            self.showPopupDetailsCorrect("Flights not selected.")

        data = c.fetchall()

        flightID = []

        #List comprehension is performed to convert the 2D array/ list into 1D list.
        for flightIDNumber in data:
            for flightIDList in flightIDNumber:
                #The flight ID will be appended to the flightID list.
                flightID.append(flightIDList)

        #If the flightID list is empty.
        #The error will be catched and a suitable message will be outputted to the console.
        if not flightID:
            print("Empty flightID list.")
        else:
            #Try except block is run to remove the flight name from the cancel flights drop down list, as
            #now when it's removed it shouldn't be in there.
            try:
                #"with connection" closes the connection automatically.
                with connection:
                    #Finds the index position of the flight name (self.data) selected by the staff to remove,
                    #and assigns the index position to the "index" variable.
                    index = self.comboBox.findText(self.data)
                    
                    #The flight name (item) will be removed using the index from the cancel drop down list box.
                    self.comboBox.removeItem(index)
                    #Resets the index position.
                    self.comboBox.setCurrentIndex(0)
 
                    #Using my "deleteFlights" function from the qjetdatabase, the flight name that the staff,
                    #selected will be removed.
                    deleteFlights(connection, flightID[0])

                    c = connection.cursor()
                    #SQL query is executed to retrieve the FlightName from the Flights table in the database.
                    c.execute("SELECT FlightName FROM Flights")
                    data = c.fetchall()

                    flightNames = []

                    #A list comprehension is performed to convert the 2D array/ list to 1D list.
                    for flightName in data:
                        for flightNameList in flightName:
                            #The flight names will be appended to the flightNames list.
                            flightNames.append(flightNameList)
                    print(flightNames)

                    #The active flights display box that contains the flights (flighr routes) for staff to view,
                    #will be reseted to blank empty box.
                    self.textEditFlights.setPlainText("")

                    flightNamesText = ""

                    #A for loop is run till the duration of the length of the flightNames list.
                    for i in range (len(flightNames)):
                        #Each flight will be appended to the flightNamesText string variable.
                        flightNamesText += "*" + flightNames[i] + "\n" + "\n"
                    #The new updated flights (flight routes) will be updated and set to the active flights display box.
                    #Now the staff can see the up to date flight names.
                    self.textEditFlights.setPlainText(flightNamesText)
                    #The flight name text colour is set to black.
                    self.textEditFlights.setStyleSheet("color: black")

            except Error as e:
                print(e)
      
    #showPopupDetailsCorrect is run whenver there is necessaray pop up that is needed to notify the member.
    #This method takes in one agruements.      
    def showPopupDetailsCorrect(self, sendInfo):  
        message = QMessageBox()
        #Sets the pop up window title to "Successful".
        message.setWindowTitle("Successful")
        #This takes in sendInfo as an arguement and this displays the main pop up message.
        message.setText(sendInfo)
        #This sets the icon of the pop up to a information symbol.
        message.setIcon(QMessageBox.Information)
        #There will be a button for the staff which they can click, and it will expand the pop up
        #to give more detail of the message.
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        #The pop up is executed.
        x = message.exec_()
        #The add flight user input box is reseted to blank empty box.
        #This is done just after the staff adds a new flight (flight route) and presses the add button.
        self.editAddFlights.setText("")

    #showPopupDetailsIncorrect is run with it recieving "sendInfo" as an arguement.
    #This method is run to inform the user with a pop up with any errors.
    def showPopupDetailsIncorrect(self, sendInfo):  
        message = QMessageBox()
        message.setWindowTitle("Unsucessful")
        message.setText(sendInfo)
        message.setIcon(QMessageBox.Warning)
    
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        x = message.exec_()
        self.editAddFlights.setText("")

    #When the staff presses the "Log out" button, the switchWindowStaff method is run and the staff window
    #will be closed. 
    def switchWindowStaff(self, staffWindow):
        staffWindow.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staffWindow = QtWidgets.QMainWindow()
    gui = showStaffWindow()
    gui.setupGuiStaff(staffWindow)
    staffWindow.show()
    sys.exit(app.exec_())
