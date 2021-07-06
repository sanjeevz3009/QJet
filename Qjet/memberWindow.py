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
#Imports the emailValid module which performs SMTP email sending operations.
from emailValid import *
#Imports hashlib module to help me with hashing the password.
import hashlib
#Imports the OS module, so it can be used to generate a arbitary charatcers
#for my salt which is uniquely generated for each new password entered.
import os

#showMemberWindow class is initated which inherits from QtWidget(QtWidgets.QWidget).
class showMemberWindow(QtWidgets.QWidget):
    #Constructor is made, __init__() function to assign values to object properties or
    #other operations that are necessaeay to do when the objects is being created.
    #The __init__() function is called automatically every time the class is 
    #being used to create a new object.

    #This constructor recieves sendAdminID as a paramater from the
    #login window(loginWindow).
    #The self parameter is a reference to the current instance of the class,
    #and is used to access variables that belong to the class.
    def __init__(self, sendMemberID):
        #super() function that will make the child class inherit all the methods and properties from its parent.
        super().__init__() 
        #The self parameter is a reference to the current instance of the class,
        #and is used to access variables that belongs to the class.   
        self.sendMemberID = sendMemberID

    #Objects can also contain methods. Methods in objects are functions that belong to the object.
    def setupGuiMember(self, memberWindow):
        #Database local location is assigned to the variable database.
        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"

        #Using the CreateConnection function in my database module, it creates the database connection
        #and assigns it to connection variable.
        connection = CreateConnection(database)
        #Creates the cursor object by calling the cursor() function method of the connection object.
        c = connection.cursor()
        #Executes a SQL statement to retrieve FirstName, Surname, Email, MobileNumber and Password.
        #from the Member table.
        c.execute("SELECT FirstName, Surname, Email, MobileNumber FROM Member WHERE MemberID = ?", [self.sendMemberID])
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a details list, so details can be appended after a list comprehension is performed
        #on the data retrieved as arrays. It will have FirstName, Surname, Email, MobileNumber and Password data.
        details = []

        #Gets the data from the database as arrays and performs a list comprehension and stores staff id in a list.
        #A nested for loop is run for this operation.
        for i in data:
            for j in i:
                details.append(j)

        #Assigns the correct items from the list to the correct variable names.
        firstName = details[0]
        surname = details[1]
        email = details[2]
        mobileNumber = details[3]

        #Setting the window title.
        memberWindow.setWindowTitle("Member page")
        memberWindow.setEnabled(True)
        memberWindow.resize(900, 700)
        #Restricting the resize minimum and maximum window size to 900 by 700.
        memberWindow.setMinimumSize(QtCore.QSize(900, 700))
        memberWindow.setMaximumSize(QtCore.QSize(900, 700))
        
        #Sets up the font style, underlines and font size for the member window title.
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        #Designs the member window title using all the QFont methods above.
        memberWindow.setFont(font)
        memberWindow.setMouseTracking(False)
        
        #Setting up the QJet logo for the log in window icon. 
        icon = QtGui.QIcon()
        #Imports the qjetLogo.png from the current folders it's in and display it on the login window.
        icon.addPixmap(QtGui.QPixmap("qjetLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        memberWindow.setWindowIcon(icon)
        
        #Positions the member title to the center of the member window.
        self.centralwidget = QtWidgets.QWidget(memberWindow)
        
        #Creates the title for the member window.
        self.title = QtWidgets.QLabel(self.centralwidget)
        #Positions the Qjet title in the member window.
        self.title.setGeometry(QtCore.QRect(330, -10, 231, 81))

        #Sets up the font style, underlines and font size for the member window title.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        #Designs the member window title using all the QFont methods above.
        self.title.setFont(font)
        #Sets the member window title to the specified title.
        self.title.setText("Member page")

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
        
        #Creates the logo box to display the logo in the member window.
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
        
        #Creates the alter/ change my details button which us used to unfreeze the input boxes
        #so the user can edit the details and save it, which will be updated to the database.
        self.buttonChangeDetails = QtWidgets.QPushButton(self.centralwidget)
        #Positions the alter/ change my details button and sets the size(dimensions).
        self.buttonChangeDetails.setGeometry(QtCore.QRect(10, 320, 411, 61))
        #Sets the text of the button.
        self.buttonChangeDetails.setText("Alter/ change my details")
        
        #Sets up the font style, underlines and font size for the button text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        #Designs the member window button text using all the QFont methods above.
        self.buttonChangeDetails.setFont(font)
        #Creates an blue outline for the log out button which glows when hovered over.
        self.buttonChangeDetails.setDefault(True)
        #When the alter/ change my details button is clicked it goes to the editDetails method.
        #Where the method unfreezes the input boxes and the user will be able to edit their details
        #and then save it which will be updated to the database.
        self.buttonChangeDetails.clicked.connect(self.editDetails)
        
        #Sets up the Welcome text which will say "Welcome FIRSTNAME SURNAME"
        self.titleWelcome = QtWidgets.QLabel(self.centralwidget)
        #Sets the text and adds the variable name firstName and surname which has the firstname and surname values
        #which was retrieved from querying the database.
        self.titleWelcome.setText("Welcome, " + firstName + " " + surname)
        #Positions the welcome text.
        self.titleWelcome.setGeometry(QtCore.QRect(10, 50, 240, 45))
        #Designs the welcome text with colour, border, size and padding.
        self.titleWelcome.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: green;
    font: bold 14px;
    min-width: 10em;
    padding: 2px;""")

        #Sets up the font style, underlines and font size for the member welcome text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        #Designs the member window welcome text using all the QFont methods above.
        self.titleWelcome.setFont(font)
        
        #This creates the information box in the member window.
        self.textEditInfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditInfo.setEnabled(False)
        self.textEditInfo.setGeometry(QtCore.QRect(10, 420, 411, 171))
        self.textEditInfo.setUndoRedoEnabled(False)
        self.textEditInfo.setPlainText("""
                                    Welcome to Qjet.
==================================
-Here you can see and change your personal details.

-You can also use the options to book/ cancel flights.

-Once your done with your tasks, you can logout using the log out button on the top right. 
            """)

        self.textEditInfo.setStyleSheet("background-color: #2094ed; color: black")

        #Creates the box that contains the labels/ text of firstname, surname, email, mobile number
        #and password text.
        self.textEditDetails = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditDetails.setEnabled(False)
        #Positions the the box of text and sets the size(dimensions).
        self.textEditDetails.setGeometry(QtCore.QRect(10, 120, 131, 191))
        self.textEditDetails.setUndoRedoEnabled(False)
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
        #Sets the text inside the text box from the queried details from the database.
        self.editFirstname.setText(firstName)
        #The input box is froze so the user cannot accidently change the details
        #unless the users intentionally wants to in that case the user can which 
        #a click of a button underneath the box.
        self.editFirstname.setEnabled(False)
        #Positions the input box for firstname and sets the size(dimensions).
        self.editFirstname.setGeometry(QtCore.QRect(140, 140, 281, 31))
        #Designs the input box with the text colour being black.
        self.editFirstname.setStyleSheet("color: black")
        
        #Creates the surname user input box.
        self.editSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.editSurname.setText(surname)
        self.editSurname.setEnabled(False)
        self.editSurname.setGeometry(QtCore.QRect(140, 170, 281, 31))
        self.editSurname.setStyleSheet("color: black")
        
        #Creates the email user input box.
        self.editEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.editEmail.setText(email)
        self.editEmail.setEnabled(False)
        self.editEmail.setGeometry(QtCore.QRect(140, 200, 281, 41))
        self.editEmail.setStyleSheet("color: black")
        
        #Creates the mobile number user input box.
        self.editMobileNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.editMobileNumber.setText(str(mobileNumber))
        self.editMobileNumber.setEnabled(False)
        self.editMobileNumber.setGeometry(QtCore.QRect(140, 240, 281, 41))
        self.editMobileNumber.setStyleSheet("color: black")
        
        #Creates a text called help in the admin window.
        self.labelHelp = QtWidgets.QLabel(self.centralwidget)
        self.labelHelp.setGeometry(QtCore.QRect(10, 385, 2, 30))
        self.labelHelp.setText("Help:")
        self.labelHelp.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: red;
    font: bold 18px;
    min-width: 2em;
    padding: 22px;""")

        #Sets up the font style, underlines and font size for the help text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        #Designs the member window help text using all the QFont methods above.
        self.labelHelp.setFont(font)
        
        #Creates the logout button.
        self.buttonLogOut = QtWidgets.QPushButton(self.centralwidget)
        #Positions the logout button and sets the size(dimensions).
        self.buttonLogOut.setGeometry(QtCore.QRect(10, 600, 101, 41))
        #Sets the text of the log out button to "Log out".
        self.buttonLogOut.setText("Logout")
        #Creates an blue outline for the log out button which glows when hovered over.
        self.buttonLogOut.setDefault(True)

        #Sets up the font style, underlines and font size for the log out button.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        #Designs the login button using all the QFont methods above.
        self.buttonLogOut.setFont(font)
        #Creates an blue outline for the log out button which glows when hovered over.
        self.buttonLogOut.setDefault(True)

        #When the log out button is clicked the switchWindowMember method is run and member window will
        #be closed.
        #A lambda function is a small anonymous function and in this case used to pass member window class
        #to switchWindowMember to close the member window.
        self.buttonLogOut.clicked.connect(lambda:self.switchWindowMember(memberWindow))

        #Creates the "Send tickets" button.
        self.buttonTicketSender = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTicketSender.setGeometry(QtCore.QRect(170, 600, 250, 41))
        self.buttonTicketSender.setText("Send my tickets to email")
        self.buttonTicketSender.setDefault(True)
        self.buttonTicketSender.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: orange;
    font: bold 18px;
    min-width: 2em;
    padding: 5px;""")

        #When the "Send tickets" button is pressed, the sendTickets method will be run.
        self.buttonTicketSender.clicked.connect(self.sendTickets)

        #Creates the password user input box.
        self.editPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.editPassword.setEnabled(False)
        self.editPassword.setGeometry(QtCore.QRect(140, 280, 281, 31))
        self.editPassword.setStyleSheet("color: black")
        #Shows a tooltip(Text popping up showing text) when hovered over the password user input box.
        self.editPassword.setToolTip("<h3>Enter your new password here.<h3>")

        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        #Creates the "View/ cancel flights:" text.
        self.labelTitleCancel = QtWidgets.QLabel(self.centralwidget)
        self.labelTitleCancel.setGeometry(QtCore.QRect(470, 80, 231, 81))
        self.labelTitleCancel.setText("View/Cancel flights:")
        self.labelTitleCancel.setFont(font)

        #Creates a text box explaining how to use the options in the member window.
        self.textEditCancel = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditCancel.setEnabled(False)
        self.textEditCancel.setGeometry(QtCore.QRect(470, 140, 241, 81))
        self.textEditCancel.setPlainText("Select your flights from the below flights booked list, and press cancel flight to cancel your flight.")
        self.textEditCancel.setStyleSheet("background-color: #2094ed; color: black")

        #Creates the drop down list box that contains the already booked flights that the member
        #can cancel.
        self.comboBoxCancel = QtWidgets.QComboBox(self.centralwidget)
        #Positions the drop down list box and sets the size(dimensions).
        self.comboBoxCancel.setGeometry(QtCore.QRect(470, 230, 300, 41))
        #When the member selects the flights to cancel from the drop down list box, the flight name will be recorded/ captured
        #and sent to the cancelFlightsData method.
        self.comboBoxCancel.activated[str].connect(self.cancelFlightsData)      

        #A try except block is ran, where inside a SQL query and operation is done to get all the flights 
        #that the member has booked which is in the FlightsBooked table, and this will be done by querying the 
        #table using the sendMemberID.
        try:
            database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"

            connection = CreateConnection(database)
            c = connection.cursor()
            #Queries the FlightID from the FlightsBooked table using the member ID.
            c.execute("SELECT FlightID FROM FlightsBooked WHERE MemberID = ?", [self.sendMemberID])
            #Fetches all the data in 2D array/ list.
            data = c.fetchall()

            #1D list to store the flight IDs queried from the FlightsBooked table using the member ID.
            flightIDs = []

            #Performs an a list comprehension on the data fetched from that database that is stored in the variable
            #"data", this is stored in a 2D array/ list.
            #To convert the 2D array/ lists to 1D list, so it's easier to loop and work through the items.
            #A nested for loop is run for this operation.
            for flightID in data:
                for flightIDList in flightID:
                    flightIDs.append(flightIDList)
            print(flightIDs)

        #If the member ID isn't found in a error case, the code woudln't and still keep running.
        #outs the specific attribute error that might occur in this sql operation.
        except AttributeError as error:
            print(error)

        #1D list to store the flight names that the user has booked, so if they users wishes they can cancel the flight booked.
        flightNamesCancel = []
        #A nested for loop is run for the duration of the length of the flightIDs 1D list.
        for i in range(len(flightIDs)):
            #A query is executed to get the flight names using the fligt IDs in the flightIDs 1D list.
            c.execute("SELECT FlightName FROM Flights WHERE FlightID = ?", [flightIDs[i]])
            #The data in this case the flight is fetched and stored in the variable data.
            #This is stored in as a 2D array/ list.
            data = c.fetchall()

            #A nested for loop is ran to append the flight names to the flightNamesCancel 1D list.
            for flightName in data:
                for flightNameList in flightName:
                    flightNamesCancel.append(flightNameList)
            print(flightNamesCancel)

        #The defualt item in the flight cance drop down list box will be "Please select the flight."
        self.comboBoxCancel.addItem("Please select the flight")
        #A for loop is run until the duration of the length of flightNamesCancel list.
        for i in range (len(flightNamesCancel)):
            #Each of the flight name is appended to the drop down list box.
            self.comboBoxCancel.addItem(flightNamesCancel[i])
        
        #Cancel button is created.
        self.buttonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCancel.setGeometry(QtCore.QRect(470, 280, 300, 28))
        self.buttonCancel.setText("Cancel flights")
        self.buttonCancel.setDefault(True)
        self.buttonCancel.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: red;
    font: bold 14px;
    min-width: 7em;
    padding: 1px;""")

        #When the cancel button is clicked, the cancelFlights method is run.
        self.buttonCancel.clicked.connect(self.cancelFlights)

        #Above the book button and widgets there will be a title called "Book".
        #"Book" title is created.
        self.labelTitleBook = QtWidgets.QLabel(self.centralwidget)
        self.labelTitleBook.setGeometry(QtCore.QRect(470, 360, 231, 81))
        self.labelTitleBook.setText("Book flights")
        self.labelTitleBook.setFont(font)

        #Another longer text box is created which contains the details of how to book the flights (guidance).
        #This is placed just underneath the "Book" title and above the book button and drop down list box that contains
        #all the flights the member can book from.
        self.textEditBook = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditBook.setEnabled(False)
        self.textEditBook.setGeometry(QtCore.QRect(470, 420, 241, 81))
        self.textEditBook.setPlainText("Select your flights from the below flights booked list, and press cancel flight to cancel your flight.")
        self.textEditBook.setStyleSheet("background-color: #2094ed; color: black")

        #The book drop down list box that will contain all the flights that the member can is created.
        self.comboBoxBook = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBook.setGeometry(QtCore.QRect(470, 510, 300, 41))

        #When the user selects a flight from the book drop down list box, it will get the data (flight name)
        #and pass the data to the bookFlightsData method.
        self.comboBoxBook.activated[str].connect(self.bookFlightsData)      

        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"

        connection = CreateConnection(database)
        c = connection.cursor()
        #All the flight names from the flights table are queried.
        c.execute("SELECT FlightName FROM Flights")
        data = c.fetchall()

        #A 1D list created to store the queried flight names.
        flightNamesBook = []
        #A list comprehension is performed using a nested for loop to convert the 2D array/ list
        #into 1D list, so it's easier and efficient to loop or go through the items in the list.
        for flightName in data:
            for flightNameList in flightName:
                flightNamesBook.append(flightNameList)
        print(flightNamesBook)

        #By default in the book drop down list box "Please select the flight" is appended.
        self.comboBoxBook.addItem("Please select the flight")
        #A for loop is run until the duration of the length of the flightNmaesBooked list.
        for i in range (len(flightNamesBook)):
            #Each flight name is appended to the book drop down list.
            self.comboBoxBook.addItem(flightNamesBook[i])
        
        #Book button is created.
        self.buttonBook = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBook.setGeometry(QtCore.QRect(470, 560, 300, 31))
        self.buttonBook.setText("Book flight")
        self.buttonBook.setDefault(True)
        self.buttonBook.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: green;
    font: bold 14px;
    min-width: 7em;
    padding: 1px;""")

        #When the book button is clicked, bookFlights method is run.
        self.buttonBook.clicked.connect(self.bookFlights)

        memberWindow.setCentralWidget(self.centralwidget)

    #bookFlightsData recieves the flight data, in this case the flight the member selects from the drop down list box.
    #This data is receieved as an arguement called "text".
    def bookFlightsData(self, text):
        #An instance variable is created and assigned to the attribute text.
        #This now contains the flight that the member has selected to book.
        self.dataBook = text

    #bookFlights method is the one that executes the SQL operation needed to book the flights that the member has choosen
    #and to update the GUI of the member window in real time as flights are booked and cancelled.
    def bookFlights(self):
        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
        connection = CreateConnection(database)
        c = connection.cursor()
        #A try except block is ran, to query the FlightID of the flight the user selected to book
        #from the book drop down list box. This is queried using the data recieved from the selected 
        #item from the book flight drop down list box, in this case the FlightName and using this
        #the FlightID is queried.
        try:
            c.execute("SELECT FlightID FROM Flights WHERE FlightName = ?", [self.dataBook])
        #If the query failed to get the FlightID using the FlightName, the self.dataBook will not be 
        #intialised, thus an attriut error will be thrown in the program. I can catch the error using
        #this except AttributeError block.
        except AttributeError as error:
            print(error)

        #The queried data will be stored in the variable "data" and it will be stored as 2D array/ list.
        data = c.fetchall()
        #A 1D list will be created to store the queried data after doing a list comprehension to convert 
        #the 2D array to a 1D list.
        flightIDs = []

        #A list comprehension is performed to convert the items from 2D array to a 1D list.
        for flightIDNumber in data:
            for flightIDList in flightIDNumber:
                #The flight ID is appended to the "flightIDs" 1D list.
                flightIDs.append(flightIDList)

        #A try except block is run to add /book the flight that the member choose to book.        
        try:
            #"with connection" automatically closes the SQL connection when updating.
            with connection:
                #The member id and the flightID of the flight the member wanted to book will be
                #stored in the "info" variable.
                info = (self.sendMemberID, flightIDs[0])
                #The flight will be booked/ inserted to the table fligthsBooked table.
                #Keeping a record that this member booked this flight using the InsertFlightsBooked function
                #from my qjetdatabase module.
                InsertFlightsBooked(connection, info)
                #The booked flights will also be updated to the cancel flights drop down list box.
                #This happens instantly live in the program/ real time update.
                #So the member if wanted can cancel the flight that they booked instantly.
                self.comboBoxCancel.addItem(self.dataBook)
                #The current index of the book drop dowen list box is found and assgined to the instance variable
                #"self.dataBook"
                self.dataBook = self.comboBoxBook.currentIndex()

                #The book flights drop down list box is reseted to the default option which is
                #"Please select the flight"
                self.comboBoxBook.setCurrentIndex(0)
                #showPopupDetailsCorrect method will be called passing two paramaters in to be recieved as arguements
                #on the other end. This pops up a notification pop up to the member.
                self.showPopupDetailsCorrect("Successful", "You flight has been booked.")

                #Another try except block is ran, to update the flights booked data in the data table, so this data can be
                #later used to calculate and visualise/ draw graphs of Qjet business data for the admin.
                try:
                    #A query is executed to get the BookedFlights integer from the Data table using the member ID.
                    c.execute("SELECT BookedFlights FROM Data WHERE MemberID = ?", [self.sendMemberID])
                    data = c.fetchall()
                    bookedFlights = []

                    #A list comprehension is perfomed to convert the 2D array to 1D list.
                    for numBookedFlights in data:
                        for numBookedFlightsList in numBookedFlights:
                            #The integer number is appended to the "bookedFlights" 1D list.
                            bookedFlights.append(numBookedFlightsList)

                    #The integer value of the number of booked flights the member has.
                    #Then it adds one to the that integer value as the member has booked a flight
                    #at this point.
                    newNumBookedFlights = bookedFlights[0] + 1

                    #The new booked flights value is updated to the Data table in the database.
                    sqlUpdate = "UPDATE Data SET BookedFlights = ? WHERE MemberID = ?"
                    info = (newNumBookedFlights, self.sendMemberID)

                    #Updated.
                    c.execute(sqlUpdate, info)
                    #Connection closed.
                    connection.commit()

                    c.execute("SELECT CancelledFlights FROM Data WHERE MemberID = ?", [self.sendMemberID])
                    data = c.fetchall()
                    cancelledFlights = []

                    for numCancelledFlights in data:
                        for numCancelledFlightsList in numCancelledFlights:
                            cancelledFlights.append(numCancelledFlightsList)

                #Except block is ran, and if the member has never booked a flight, when updating the record,
                #it will throw an error.
                except:
                    with connection:
                        #As at this point the member has decided to book a flight, so the integer value of one will be added/
                        #inserted added.
                        sql = "INSERT INTO Data(MemberID, BookedFlights) VALUES(?, ?)"
                        info = (self.sendMemberID, "1")
                        #The opertation is executed.
                        c.execute(sql, info)

                        #Also the cancelled flights for the member will be set to 0 in the Data table in the database.
                        #As the member has booked a flight for the first time and so far they haven't cancelled any flights.
                        sqlUpdate = "UPDATE Data SET CancelledFlights = ? WHERE MemberID = ?"
                        info2 = ("0", self.sendMemberID)
                        #The operation is executed.
                        c.execute(sqlUpdate, info2)
                        #Connection is closed.
                        connection.commit()

        #Except block is ran if the member hasn't selected a flight to book, and pressed the book button.
        except:
            self.showPopupDetailsIncorrect2("Please select a flight to book.")

    #The flight the member wants to cancel is recieved as an arguement in a variable called
    #"text".
    def cancelFlightsData(self, text):
        #The flight name which is recieved in the "text" arguement is assgiend to the instance "self.dataCancel".
        self.dataCancel = text

    #cancelFlights method is run the member has selected a flight to cancel and pressed the cancel button.
    #cancelFlights method is used to delete/ update the flightsBooked table, for the flight that the member
    #wants to cancel.
    def cancelFlights(self):
        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
        connection = CreateConnection(database)
        c = connection.cursor()

        #A try except block is ran to query the FlightID using the FlightName, that the member selected to
        #cancel the flight from the cancel drop down list box.
        try:
            c.execute("SELECT FlightID FROM Flights WHERE FlightName = ?", [self.dataCancel])
        except AttributeError as error:
            print(error)

        data = c.fetchall()
        flightID = []

        for flightIDNumber in data:
            for flightIDList in flightIDNumber:
                flightID.append(flightIDList)

        #If the flightID 1D list doesn't contain after list comprehesnion as if there was no data gained from querying,
        #the showPupupDetailsIncorrect2 method will be run with a suitable text sent as paramater.
        if not flightID:
            #This pops up a notification pop up to the member.
            self.showPopupDetailsIncorrect2("Please select a flight to cancel.")
        else:
            #A try except block is run to update/ delete the flight from the flightsBooked table for the flight,
            #that the member selected to cancel.
            try:
                with connection:
                    #Using the dataCancel instance variable that contains the FlightName that the member chose to cancel,
                    #the index position is found in the cancel flights drop down list box.
                    index = self.comboBoxCancel.findText(self.dataCancel)
                    
                    #Using the index position the flight name removed/ deleted real time from the cance flights,
                    #drop down list box.
                    self.comboBoxCancel.removeItem(index)
                    #The index position is resetted.
                    self.comboBoxCancel.setCurrentIndex(0)
                    #The flight the member wanted to delete, will be deleted.
                    #The SQL operation will be executed using the deleteFlightsBooked function from my
                    #qjetdatabase module.
                    deleteFlightsBooked(connection, flightID[0])

                    #The default selection for the cancel drop down list is set.
                    self.dataCancel = self.comboBoxCancel.currentIndex()

                    #Once all the above code as been executed, the showPopDetailsCorrect method will be run, with being passed,
                    #two paramaters. 
                    #This pops up a notification pop up to the member.
                    self.showPopupDetailsCorrect("Successful", "Your flight has been cancelled.")

                    #Another try and except block is ran to query the integer number for the cancelled flights for the member,
                    #from the Data table. 
                    try:
                        c.execute("SELECT CancelledFlights FROM Data WHERE MemberID = ?", [self.sendMemberID])
                        data = c.fetchall()
                        cancelledFlights = []

                        #A list comprehension is ran to convert 2 Array into a 1D list.
                        for numCancelledFlights in data:
                            for numCancelledFlightsList in numCancelledFlights:
                                cancelledFlights.append(numCancelledFlightsList)

                        #The integer value for the number of cancelled flights, is taken and added one to it.
                        #This is stored in the newNumCancelledFlights variable.
                        newNumCancelledFlights = cancelledFlights[0] + 1

                        #The number of CancelledFlights data from the "Data" table is updated with the
                        #new value using the member ID.
                        sqlUpdate = "UPDATE Data SET CancelledFlights = ? WHERE MemberID = ?"
                        info = (newNumCancelledFlights, self.sendMemberID)

                        #The update operation is executed.
                        c.execute(sqlUpdate, info)
                        #The connection is closed.
                        connection.commit()

                    #Except block is ran if there was any error caused from the SQL operation and the specific
                    #error will be printed to the console, so it can be debugged.
                    except Error as e:
                        print(e)
            #Except block is ran if there was any error caused from the SQL operation and the specific
            #error will be printed to the console, so it can be debugged.
            except Error as e:
                print(e)
    
    #When the member presses the "Send tickets" button, the sendTickets method is run.
    def sendTickets(self):
        #An instance is created and emailSenderTicktes is instantiated and assigned to the variable a.
        #Also instance vriable sendMemberID is passed in as parameter, so it can be recieved as an arguement
        #on the other end.
        a = emailSenderTickets(self.sendMemberID)
        #From emailSenderTickets class, sendTickets method is executed and a email will be sent to the member
        #with their booked flights tickets.
        a.sendTickets()
        #showPopupDetailsCorrect method will be run with two paramaters being passed in.
        #This pops up a notification pop up to the member.
        self.showPopupDetailsCorrect("Successful", "Your flight tickets has been sent to your email.")

    #When the member presses the "Log out" button, the switchWindowMember method is run and the member window
    #will be closed.
    def switchWindowMember(self, memberWindow):
        memberWindow.close()
    
    #When the user pressed "Alter/ change my details" button, the editDetails method will be run.       
    def editDetails(self):
        #All the user input boxes will be unfroze, so the member can input their latest/ new details.
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
        
    #saveDetails method is run to update the member details.
    def saveDetails(self):
        database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
        connection = CreateConnection(database)

        #Only if the password is more than 8 characters long, the rest of the code will be executed.
        if len(self.editPassword.text()) < 8:
            #showPopupDetailsIncorrect2 method will be run with one paramater being passed in.
            #This pops up a notification pop up to the member.
            self.showPopupDetailsIncorrect2("Password has to be more than 8 characters.")
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

                #The updateMember function will be run from my qjetdatabase module I have imported.
                updateMember(connection, (self.editFirstname.text(), self.editSurname.text(), 
                            self.editEmail.text(), self.editMobileNumber.text(), hashPasswordHex, saltHex, self.sendMemberID))
                
                #The user input boxes will freeze again, which will make it not possible for accidental changed to the,
                #member details.
                self.editFirstname.setEnabled(False)
                self.editSurname.setEnabled(False)
                self.editEmail.setEnabled(False)
                self.editMobileNumber.setEnabled(False)
                self.editPassword.setEnabled(False)
                
                #The button text will be changed back to "Alter/ change my details" from "Save details".
                #This is a form of polymorphism.
                self.buttonChangeDetails.setText("Alter/ change my details")
                #If the member wishes to change the details again, the editDetails method will be run again.
                self.buttonChangeDetails.clicked.connect(self.editDetails)
    
    #showPopupDetailsCorrect is run whenver there is necessaray pop up that is needed to notify the member.
    #This method takes in two agruements.
    def showPopupDetailsCorrect(self, popUpText, sendInfo):
        message = QMessageBox()
        #Takes in the popUpText as an agruement, and this sets the pop up title.
        message.setWindowTitle(popUpText)
        #This takes in sendInfo as an arguement and this displays the main pop up message.
        message.setText(sendInfo)
        #This sets the icon of the pop up to a information symbol.
        message.setIcon(QMessageBox.Information)
        #There will be a button for the member which they can click, and it will expand the pop up
        #to give more detail of the message.
        message.setDetailedText("Details have been saved to the database.")
        #The buttons are set in this case the "Cancel" and the "Ok" button.
        message.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        #The pop up is executed.
        x = message.exec_()   

    #showPopupDetailsIncorrect2 method is ran, with it taking in one arguement.
    #This can be used to pop up a notification to the member, for any unsuccessful or any errors.
    def showPopupDetailsIncorrect2(self, info):
        message = QMessageBox()
        message.setWindowTitle("Unsuccessful")
        message.setText(info)
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        x = message.exec_() 
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    memberWindow = QtWidgets.QMainWindow()
    gui = showMemberWindow()
    gui.setupGuiMember(memberWindow)
    memberWindow.show()
    sys.exit(app.exec_())
    
    
    
