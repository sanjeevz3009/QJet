# QJet - Airline Booking & Management System
### Usuage
* `pip install -r requirements.txt` to install the required modules and files.
* Open the `LoginWindow.py` file from Qjet folder to start the program.
### Features
* Users will be able to create accounts, select and book flights, cancel flights, change their personal details and reset their login details via an email sent to them.
* Staffs will be able to cancel flights for users to book, change their personal details, reset their login details and add new flights and prices for the users to book.
* Admin will be able to create and delete staff accounts, change their personal details and reset their login details. Admins will also be able to see some insights about the company, such as booked and cancelled flights data in various different graphs. Admins will also have the ability to export these data into a excel file.
### Future improvements
* Improved GUI.
* Modularising the code into more smaller files for maintainability.
### Files
>
* `loginWindow.py` is the start of the application. It checks for different user types such as customers, staffs and admins. Then takes them to the suitable page/ window for the user.
* `memberWindow.py` contains the code for the member page/ window.
* `staffWindow.py` contains the code for the staff page/ window.
* `adminWindow.py` contains the code for the admin page/ window.
* `registerWindow.py` contains the code for the register page/ window.
* `emailValid.py` contains the code to send emails, in this case used for login details resetting.
* `qjetdatabase.py` contains the code to create the database for the application.
* `visualiseData.py` contains code to draw and display graphs from the data gathered by the application.
