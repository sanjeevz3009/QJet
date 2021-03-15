#Importing the necessary modules.
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
#Imports the pop up notifications widgets.
from PyQt5.QtWidgets import QMessageBox

#Imports system.
import sys

#Imports the other python files as modules.
#Imports the database file.
from qjetdatabase import *
#Imports the login window.
from loginWindow import *
#Imports the graphing and exporting to text and excel file module.
from visualiseData import *
#To help with my queue operations I import queue from Queue.
from queue import Queue
#Imports the hashing module to help me with hashing the password.
import hashlib
#Imports the OS module, so it can be used to generate a arbitary charatcers
#for my salt which is uniquely generated for each new password entered.
import os

#showAdminWindow class is intiated which inherits from QtWidget(QtWidgets.QWidget)
class showAdminWindow(QtWidgets.QWidget):
    #Constructor is made, __init__() function to assign values to object properties or
    #other operations that are necessary to do when the objects is being created.
    #The __init__() function is called automatically every time the class is 
    #being used to create a new object.

    #This constructor recieves sendAdminID as a paramater from the
    #login window(loginWindow).
    #The self parameter is a reference to the current instance of the class,
    #and is used to access variables that belong to the class.
    def __init__(self, sendAdminID):
        #super() function that will make the child class inherit all the methods and properties from its parent.
        super().__init__()    
        #The self parameter is a reference to the current instance of the class,
        #and is used to access variables that belongs to the class.
        self.sendAdminID = sendAdminID

    #Objects can also contain methods. Methods in objects are functions that belong to the object.
    def setupGuiAdmin(self, adminWindow):
        #Database local location is assigned to the variable "database".
        database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
        #Using the "CreateConnection" function in my database module, it creates the database connection
        #and assigns it to "connection" variable.
        connection = CreateConnection(database)
        #Creates the cursor object by calling the cursor() function method of the connection object.
        c = connection.cursor()

        #Executes a SQL statement to retrieve the FirstName, Surname, Email, MobileNumber and Password.
        #from the Admin table.
        c.execute("SELECT FirstName, Surname, Email, MobileNumber FROM Admin WHERE AdminID = ?", [self.sendAdminID])
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Creates a details list, so details can be appended after a list comprehension is performed
        #on the data retrieved as arrays. It will have FirstName, Surname, Email, MobileNumber and Password data.
        details = []

        #Gets the data from the database as arrays and performs a list comprehension and stores staff ID in a list.
        for detail in data:
            for detailList in detail:
                details.append(detailList)

        #Assigns the correct items from the list to the correct variable names.
        firstName = details[0]
        surname = details[1]
        email = details[2]
        mobileNumber = details[3]
        
        adminWindow.setEnabled(True)
        adminWindow.resize(900, 700)
        #Restricting the resize minimum and maximum window size to 900 by 700.
        adminWindow.setMinimumSize(QtCore.QSize(900, 700))
        adminWindow.setMaximumSize(QtCore.QSize(900, 700))

        #Setting the window title.
        adminWindow.setWindowTitle("Admin - page")

        #Positions the admin title to the center of the admin window.
        self.centralwidget = QtWidgets.QWidget(adminWindow)

        #Creates the title in the admin window.
        self.title = QtWidgets.QLabel(self.centralwidget)
        #Positions the Qjet title in the admin window.
        self.title.setGeometry(QtCore.QRect(370, -10, 211, 81))
        #Sets the admin window title to the specified title.
        self.title.setText("Admin Page")
        
        #Sets up the font style, underlines and font size for the admin window title.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        #Designs the admin window title using all the QFont methods above.
        self.title.setFont(font)

        #Setting up the QJet logo for the admin in window icon. 
        icon = QtGui.QIcon()
        #Imports the qjetLogo.png from the current folders it's in and display it on the admin window icon.
        icon.addPixmap(QtGui.QPixmap("qjetLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        adminWindow.setWindowIcon(icon)

        #Sets up the background image.
        self.background = QtWidgets.QLabel(self.centralwidget)
        #Positions the background image.
        self.background.setGeometry(QtCore.QRect(0, 0, 901, 700))
        self.background.setText("")
        #Imports the aviation.png from the current folder it's in.
        self.background.setPixmap(QtGui.QPixmap("aviation.png"))
        #Makes the image less blurry by importing and placing it to scale.
        self.background.setScaledContents(True)
        self.background.setWordWrap(False)

        #Brings the title front over the background.
        self.title.raise_()

        #Sets up the Welcome text which will say "Welcome FIRSTNAME + SURNAME"
        self.titleWelcome = QtWidgets.QLabel(self.centralwidget)
        #Positions the welcome text.
        self.titleWelcome.setGeometry(QtCore.QRect(10, 50, 200, 50))
        #Sets the text and adds the variable name firstName and surname which has the firstname and surname data
        #which is retrieved from querying the database, sepecifically the admin table.
        self.titleWelcome.setText("Welcome, " + firstName + " " + surname)
        #Designs the welcome text with colour, border, size and padding.
        self.titleWelcome.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: green;
    font: bold 14px;
    min-width: 10em;
    padding: 12px;""")

        #Sets up the font style, underlines and font size for the admin welcome text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        #Designs the admin window welcome text using all the QFont methods above.
        self.titleWelcome.setFont(font)

        #Creates the logout button.
        self.buttonLogout = QtWidgets.QPushButton(self.centralwidget)
        #Positions the logout button and sets the size(dimensions).
        self.buttonLogout.setGeometry(QtCore.QRect(10, 600, 101, 41))
        #Sets the text of the logout button.
        self.buttonLogout.setText("Log out")

        #Sets up the font style, underlines and font size for the log out button.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        #Creates an blue outline for the log out button which glows when hovered over.
        self.buttonLogout.setDefault(True)
        #Designs the login button using all the QFont methods above.
        self.buttonLogout.setFont(font)

        #When the log out button is clicked the switchWindowAdmin method is run and admin window will
        #be closed.
        #A lambda function is a small anonymous function and in this case used to pass adminWindow
        #to switchWindowAdmin to close the admin window.
        self.buttonLogout.clicked.connect(lambda:self.switchWindowAdmin(adminWindow))

        #Creates the "My personal details:" text in the admin window.
        self.titlePersonalDetails = QtWidgets.QLabel(self.centralwidget)
        #Positions the text and sets the size(dimensions).
        self.titlePersonalDetails.setGeometry(QtCore.QRect(158, 165, 240, 30))
        #Sets the text to the specified text below.
        self.titlePersonalDetails.setText("My personal details:")
        #Designs the welcome text with colour, border, size and padding.
        self.titlePersonalDetails.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: red;
    font: bold 18px;
    min-width: 2em;
    padding: 22px;""")

        #Sets up the font style, underlines and font size for the "My personal details" text.
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        #Designs the "My personal details" text using all the QFont methods above.
        self.titlePersonalDetails.setFont(font)

        #Creates the box that contains the labels/ text of firstname, surname, email, mobile number
        #and password text.
        self.textEditDetails = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditDetails.setEnabled(False)
        #Positions the the box of text and sets the size(dimensions).
        self.textEditDetails.setGeometry(QtCore.QRect(10, 180, 131, 191))
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
        #Unless alter/change details button is clicked, where the box will unfreeze
        #so the user can edit the details and click the save details button to save 
        #the new details to the database.
        self.editFirstname = QtWidgets.QLineEdit(self.centralwidget)
        #The input box is froze so the user cannot accidently change the details
        #unless the users intentionally wants to in that case the user can with 
        #a click of a button underneath the box.
        self.editFirstname.setEnabled(False)
        #Positions the input box for firstname and sets the size(dimensions).
        self.editFirstname.setGeometry(QtCore.QRect(140, 200, 281, 31))
        #Sets the text inside the text box from the queried details from the database.
        self.editFirstname.setText(firstName)
        #Designs the input box with the text colour being black.
        self.editFirstname.setStyleSheet("color: black")

        #Creates the surname user input box.
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

        #Creates the mobile number user input box.
        self.editMobileNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.editMobileNumber.setEnabled(False)
        self.editMobileNumber.setGeometry(QtCore.QRect(140, 300, 281, 41))
        self.editMobileNumber.setText(str(mobileNumber))
        self.editMobileNumber.setStyleSheet("color: black")

        #Creates the alter/ change my details button which us used to unfreeze the input boxes
        #so the user can edit the details and save it, which will be updated to the database, 
        #specifically the admin table in this case.
        self.buttonChangeDetails = QtWidgets.QPushButton(self.centralwidget)
        #Positions the alter/ change my details button and sets the size(dimensions).
        self.buttonChangeDetails.setGeometry(QtCore.QRect(10, 385, 411, 71))
        #Sets the text of the button.
        self.buttonChangeDetails.setText("Alter/ change my details")
       
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.buttonChangeDetails.setFont(font)

        #Creates an blue outline for the log out button which glows when hovered over.
        self.buttonChangeDetails.setDefault(True)
        
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

        #Creates the logo box to display the logo in the admin window.
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

        #Creates the box to display the staff email.
        self.textEditEmail = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditEmail.setEnabled(True)
        #Positions the the box and sets the size(dimensions).
        self.textEditEmail.setGeometry(QtCore.QRect(430, 200, 451, 171))
        #It's is ready only and can't be edited.
        self.textEditEmail.setReadOnly(True)

        #Specifies the database file location to the database variable which will store the location.
        database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"

        #The database connection is created using the database location.
        #CreateConnection from my database module is used to create the database connection.
        #This is assigned to the variable connection.
        connection = CreateConnection(database)

        #Creates the cursor object by calling the cursor() function method of the connection object.
        c = connection.cursor()

        #Executes a sql statement to retrieve Email from the Staff table.
        c.execute("SELECT Email FROM Staff")
        #Calls the fetchall() method of the cursor object to fetch the data.
        data = c.fetchall()

        #Assigns a empty string to the emailText variable.
        #So later string operations/ manipulation can be performed.
        emailText = ""

        #For email in data array it will loop through and adds each staff email address to the emailText variable string.
        #A list comprehension will also be performed to adds the staff emails to the emailText variable string.
        for email in data:
            #As it adds to the staff emails to the emailText \n is used to space everything out.
            emailText += "*" + email[0] + "\n" + "\n"

        #Sets the emailText to the box that was created tp display the staff accounts.
        self.textEditEmail.setPlainText(emailText)
        #Sets the text colour to black.
        self.textEditEmail.setStyleSheet("color: black")

        #Creates the title "Staff" above the text list box which has the staff accounts displayed to the user.
        self.titleStaff = QtWidgets.QLabel(self.centralwidget)
        self.titleStaff.setGeometry(QtCore.QRect(430, 140, 351, 81))
        self.titleStaff.setText("Staff")

        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        self.titleStaff.setFont(font)

        #Creates the title above the drop down list to remove/ delete staff account.
        self.titleDelete = QtWidgets.QLabel(self.centralwidget)
        self.titleDelete.setGeometry(QtCore.QRect(430, 370, 471, 41))
        self.titleDelete.setText("Select the staff account to delete")

        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        self.titleDelete.setFont(font)

        #Creates the drop down list box.
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        #Positions the drop down list box and sets the size(dimensions).
        self.comboBox.setGeometry(QtCore.QRect(430, 470, 311, 31))

        #Adds the first default item into the drop down list box.
        self.comboBox.addItem("Please select the staff account")

        #For email in data all the staff email addresses will be appended to the drop down list box.
        #A list comprehension is performed here as well.
        for email in data:
            self.comboBox.addItem(email[0])

        #When the admin selects the staff account from the drop down list box, the email address will be recorded/ captured
        #and sent to the delStaffsData method.
        self.comboBox.activated[str].connect(self.delStaffsData)      

        #Creates the information box which contains the info to guide the admin into how to delete the staff accounts and
        #use the interface.
        self.textEditDelete = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditDelete.setEnabled(False)
        self.textEditDelete.setGeometry(QtCore.QRect(430, 410, 451, 51))
        self.textEditDelete.setPlainText("Select the staff account from the list below and press the remove button to remove the staff account.")
        self.textEditDelete.setStyleSheet("color: black")

        #Creates the remove button.
        self.buttonRemove = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRemove.setGeometry(QtCore.QRect(750, 470, 7, 31))
        self.buttonRemove.setText("Remove")
        self.buttonRemove.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: red;
    font: bold 14px;
    min-width: 7em;
    padding: 1px;""")
        
        #When the remove button is pressed the delStaffs method is executed.
        self.buttonRemove.clicked.connect(self.delStaffs)

        #Creates a info box which guides the admin on how and what does the various buttons such as graphs and exports do.
        self.textEditInfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditInfo.setEnabled(False)
        self.textEditInfo.setGeometry(QtCore.QRect(430, 510, 451, 51))
        self.textEditInfo.setPlainText("Use the options below to see insights about Qjet as graphs. Or export the data to excel file.")
        self.textEditInfo.setStyleSheet("color: black")

        #Creates a button called View booked and cancelled flights data(Grouped bar graph).
        self.buttonViewBarGraph = QtWidgets.QPushButton(self.centralwidget)
        self.buttonViewBarGraph.setGeometry(QtCore.QRect(430, 570, 450, 31))
        self.buttonViewBarGraph.setText("View booked and cancelled flights data(Grouped bar graph)")

        #When the button is clicked it will go to the showBarGraph method.
        self.buttonViewBarGraph.clicked.connect(self.showBarGraph)

        #Creates a text called help in the admin window.
        self.titleHelp = QtWidgets.QLabel(self.centralwidget)
        self.titleHelp.setGeometry(QtCore.QRect(10, 465, 2, 30))
        self.titleHelp.setText("Help:")
        self.titleHelp.setStyleSheet("""background-color: white; border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: red;
    font: bold 18px;
    min-width: 2em;
    padding: 22px;""")

        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)

        self.titleHelp.setFont(font)

        #A info box is created where it gives a overiew for the admin what they can do in the admin window.
        self.textEditWelcome = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditWelcome.setEnabled(False)
        self.textEditWelcome.setGeometry(QtCore.QRect(10, 500, 411, 91))
        self.textEditWelcome.setPlainText("Welcome to Qjet admin page. Here you can view insights of Qjet, view business data and even alter/ change your personal details.")
        self.textEditWelcome.setStyleSheet("color: black")

        #Creates a button called Total booked vs cancelled flights(Pie chart).
        self.buttonPieChart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPieChart.setGeometry(QtCore.QRect(430, 610, 255, 31))
        self.buttonPieChart.setText("Total booked vs cancelled flights(Pie chart)")

        #When the button is clicked showPieChart method is executed.
        self.buttonPieChart.clicked.connect(self.showPieChart)

        #Creates a button called Export to text file and excel.
        self.buttonExportText = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExportText.setGeometry(QtCore.QRect(690, 610, 190, 31))
        self.buttonExportText.setText("Export to text file and excel")

        #When the button is clicked exportTextExcel method is executed.
        self.buttonExportText.clicked.connect(self.exportTextExcel)

        adminWindow.setCentralWidget(self.centralwidget)     

    #Method which unfreezes the input boxes so the admin can edit their details.
    def editDetails(self):
        #The input boxes are set to true so it can be editable.
        self.editFirstname.setEnabled(True)
        self.editSurname.setEnabled(True)
        self.editEmail.setEnabled(True)
        self.editMobileNumber.setEnabled(True)
        self.editPassword.setEnabled(True)
            
        #There is a polymorphism happening here as the button name is overriden to Save Details after
        #the button has been clicked to alter the admin details.
        self.buttonChangeDetails.setText("Save details")

        #When the button is pressed again saveDetails method is run.
        self.buttonChangeDetails.clicked.connect(self.saveDetails)   

    #Freezes the input boxes so the user can't accidently edit the details and updates the new altered/ changed
    #details to the database.
    def saveDetails(self):
        print("Running!")
        database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
        connection = CreateConnection(database)
        #With connection us used so after the connection is successfully established the connection will also
        #will be automatically closed once all the necessaray code is ran. We don't need to close the connection
        #manually.

        if len(self.editPassword.text()) < 8:
            self.showPopupDetailsIncorrect("Password has to be more than 8 characters.", "")
        else:
            with connection:
                #From my qjetdatabase module the updateAdmin function is called and the updated details are passed in as paramaters
                #to be retrieved on the other end as arguements.

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

                updateAdmin(connection, (self.editFirstname.text(), self.editSurname.text(), 
                            self.editEmail.text(), self.editMobileNumber.text(), hashPasswordHex, saltHex, self.sendAdminID))

                #The input boxes will be frozen so the user doesn't accidently edit the details.
                self.editFirstname.setEnabled(False)
                self.editSurname.setEnabled(False)
                self.editEmail.setEnabled(False)
                self.editMobileNumber.setEnabled(False)
                self.editPassword.setEnabled(False)
                
                #Now the button text will be changed back to and set to Alter/ change my details.
                #This is also consiered polymorphism and a example of overriding.
                self.buttonChangeDetails.setText("Alter/ change my details")
                
                #If the button is to be clicked again, the editDetails method will be ran again and so on.
                self.buttonChangeDetails.clicked.connect(self.editDetails)

    #delStaffsData method recuieves the selected staff account to delete from the drop down list box.
    #The data is recieved as parameters.    
    def delStaffsData(self, text):
        #A instance called data is created and assigned to a property called text.
        #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        self.data = text 
        print(self.data)
        
    def delStaffs(self):
        database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
        connection = CreateConnection(database)
        c = connection.cursor()

        #A try and except to ran so everything run smoothly and errors are catched without breaking the code.
        #A try and except is ran to query StaffID from the Staff table using the email address selected by the admin
        #from the drop down list box which is sent to the method delStaffData as a paramater and now can be used to
        #query the database for the StaffID so they can be removed from the database.
        try:
            c.execute("SELECT StaffID FROM Staff WHERE Email = ?", [self.data])
        #Except AttributeError will be ran and printed to the console if the data hasn't been sent from the drop down list box 
        #which the admin selected.
        except AttributeError as error:
            print(error)

        #Data is fetched.
        data = c.fetchall()
        staffsIDs = []

        #A list comprehension is performed to get the staffID.
        for staffID in data:
            for staffIDList in staffID:
                staffsIDs.append(staffIDList)

        #If the staffID list is empty the error will be catched and popped up to the user as a pop up notification.
        if not staffsIDs:
            sendError = "Please select a valid staff account."
            sendErrorDetail = "Empty staffIDs list."
            #The errors will be sent to the showPopupDetailsIncorrect and the sendError and sendErrorDetail as arguements.
            self.showPopupDetailsIncorrect(sendError, sendErrorDetail)
        #If the staffID list is not empty.
        else:
            #A try and except will be run to find the email address in the drop down list and remove it first.
            try:
                #With connection is used so the connection is opened and closed automatically.
                with connection:
                    #index is to a findText method where it would try to find the index of the staff email address
                    #in the drop down list box.
                    index = self.comboBox.findText(self.data)

                    #The item(staff email address) is removed from the drop down list using it's index position
                    #which was retrieved ans stored in the index variable.
                    self.comboBox.removeItem(index)
                    #The Please select staff account to remove text will be displayed as defualt again after the user removes
                    #the selected staff accout by clicking the remove button.
                    self.comboBox.setCurrentIndex(0)

                    #Initialising a queue 
                    q = Queue(maxsize = len(staffsIDs)) 

                    #qsize() give the maxsize of the Queue 
                    print("Current size of the queue:", q.qsize())

                    #Adding of element to queue
                    for i in range(len(staffsIDs)):
                        q.put(staffsIDs[i]) 
                        
                    print("Current size of the queue:", q.qsize())

                    #Prints if the queue is full or not.
                    print("\nQueue being full: ", q.full())

                    #The deleteStaff function is called from my qjetdatabase module and the staff account is removed from the 
                    #Staff table in the database.
                    deleteStaff(connection, q.get())

                    print("\nEmpty: ", q.empty()) 
                    q.put(1) 
                    print("\nEmpty: ", q.empty())  
                    print("\nQueue being full: ", q.full())

                    c = connection.cursor()
                    #The emails are queried again from the Staff table.
                    c.execute("SELECT Email FROM Staff")
                    #All the emails are fetched and stored in an array.
                    data = c.fetchall()

                    emails = []
                    #A list comprehension is performed to get all the emails and store it in a list.
                    for email in data:
                        for emailList in email:
                            emails.append(emailList)
                    print(emails)

                    #The box that displays the staff accounts will be updated with the new staffs after the admin removes
                    #the staff account they wanted remove.
                    self.textEditEmail.setPlainText("")
                    emailText = ""

                    #For email for the length of emails list the for loop is ran.
                    #The emails are added to the emailText variable string.
                    for email in range(len(emails)):
                        #The emails are added to the emailText variable string and \n is used to space the emails out.
                        emailText += "*" + emails[email] + "\n" + "\n"

                    #The updated staff emails list after the admin removes a staff account is displayed.
                    #The new updated staff email info is set to the staff email display box.
                    self.textEditEmail.setPlainText(emailText)
                    self.textEditEmail.setStyleSheet("color: black")

                    #A pop up will be shown to the user.
                    #showPopupDetailsCorrect method will be ran and Staff account removed text will be passed into the method
                    #as arguements.
                    self.showPopupDetailsCorrect("Staff account removed.")    

            #Any error catched will be printed to the console.
            except Error as e:
                print(e)

    #showBarGraph method is ran when the admin clicks View booked and cancelled flights data(Grouped bar graph) button.
    def showBarGraph(self):
        #From my visualiseData module the start class and a object is created.
        #The showGroupedBarGraph method from the start class is called and excecuted
        #where it will then collect all the data from the database and plot a grouped bar graph using matplotlib and display to 
        #admin in a new window.
        show = start()
        show.showGroupedBarGraph()

    #showPieChart method is ran when the admin clicks Total booked vs cancelled flights(Pie chart) button.
    def showPieChart(self):
        #From my visualiseData module the start class and a object is created.
        #The showPieChart method from the start class is called and excecuted
        #where it will then collect all the data from the database and plot a pieChart using matplotlib and display to 
        #admin in a new window.
        show = start()
        show.showPieChart()

    #showPieChart method is ran when the admin clicks Export to text file and excel button.
    def exportTextExcel(self):
        #From my visualiseData module the start class and a object is created.
        #The exportToText and exportToExcelmethod from the start class is called and excecuted
        #where it will then collect all the data from the database and export the Qjet business data to 
        #text file format and to a excel spreadsheet.
        export = start()
        export.exportToText()
        export.exportToExcel()
        #A pop up notification will be popped up to the user saying the exports has been completed.
        #showPopupDetailsCorrect method is called and Exported to text and excel file text is passed in as 
        #paramater to be recieved as arguement on showPopupDetailsCorrect method.
        self.showPopupDetailsCorrect("Exported to text and excel file.")
    
    #A pop up notification method.
    #It retrieves a text or a variable as a arguement.
    def showPopupDetailsCorrect(self, info):
        message = QMessageBox()
        #Sets the pop up window title text to Successful.
        message.setWindowTitle("Successful")
        #Sets the main text on the pop up window using the text from the arguement recieved.
        message.setText(info)
        #The logo will be a information logo in the pop up window.
        message.setIcon(QMessageBox.Information)
        #message.setInformativeText("Information!")
        #message.setDetailedText("")

        #message.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        #Pop up is executed and popped up and shown to the user.
        x = message.exec_()

    def showPopupDetailsIncorrect(self, sendError, sendErrorDetail):
        message = QMessageBox()
        message.setWindowTitle("Unsuccessful")
        message.setText(sendError)
        message.setIcon(QMessageBox.Warning)
        #message.setInformativeText("Information!")
        message.setDetailedText(sendErrorDetail)

        message.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)
        x = message.exec_()

    #When the logout button is clicked the switchWindowAdmin method is ran and executed.
    #Recieving staffWindow as arguement.
    def switchWindowAdmin(self, adminWindow):
        #The staffWindow is closed.
        adminWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminWindow = QtWidgets.QMainWindow()
    gui = showAdminWindow()
    gui.setupGuiAdmin(adminWindow)
    adminWindow.show()
    sys.exit(app.exec_())
