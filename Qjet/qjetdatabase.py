#Imports the sqlite3 module.
import sqlite3 
from sqlite3 import Error 

#Creates the database connection.
def CreateConnection(db_file):
    #Creates a database connection to the SQlite database.
    
    #Sets the connetion to none.
    #Tries to connect to the database if not prints the error and closes the connection.
    #Try except is used to catch the error if it occurs.
    connection = None;
    try:
        #Creates a connection object using the connect() function of the sqlite3 module.
        connection = sqlite3.connect(db_file)
    #Catches the error and prints the exact error that occured.
    except Error as e:
        print(e)
    
    #returns the sql connection.
    return connection
            
def CreateTable(connection, CreateTableSql):
    #Tries to get the connection from CreateConnection function.
    #Creates a table from the CreateTableSql statement.
    try:
        #Creates the cursor object by calling the cursor() function method of the connection object.
        c = connection.cursor()
        c.execute(CreateTableSql)
    except Error as e:
        print(e)       

def Creating():
    #Database location specified.
    database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
    
    #Creates the member table.
    CreateMemberTable = """
    CREATE TABLE IF NOT EXISTS Member(
        MemberID VARCHAR(4) PRIMARY KEY NOT NULL,
        FirstName TEXT,
        Surname TEXT,
        Email TEXT,
        MobileNumber INTEGER,
        Hash TEXT NOT NULL,
        Salt TEXT NOT NULL
    );"""
    
    CreateStaffTable = """
    CREATE TABLE IF NOT EXISTS Staff(
        StaffID VARCHAR(4) PRIMARY KEY NOT NULL,
        FirstName TEXT,
        Surname TEXT,
        Email TEXT,
        MobileNumber INTEGER,
        Hash TEXT NOT NULL,
        Salt TEXT NOT NULL
    );"""

    CreateAdminTable = """
    CREATE TABLE IF NOT EXISTS Admin(
        AdminID VARCHAR(4) PRIMARY KEY NOT NULL,
        FirstName TEXT,
        Surname TEXT,
        Email TEXT,
        MobileNumber INTEGER,
        Hash TEXT NOT NULL,
        Salt TEXT NOT NULL
    );"""
    
    CreateFlights = """
    CREATE TABLE IF NOT EXISTS Flights(
        FlightID VARCHAR(4) PRIMARY KEY NOT NULL,
        FlightName TEXT NOT NULL
    );"""
    
    CreateFlightsBooked = """
    CREATE TABLE IF NOT EXISTS FlightsBooked(
        MemberID VARCHAR(4),
        FlightID VARCHAR(4),
        PRIMARY KEY(MemberID, FlightID),
        FOREIGN KEY(MemberID) REFERENCES Member(MemberID),
        FOREIGN KEY(FlightID) REFERENCES Flights(FlightID)
    );"""

    CreateDataTable = """
    CREATE TABLE IF NOT EXISTS Data(
    MemberID VARCHAR(4),
    BookedFlights INTEGER,
    CancelledFlights INTEGER,
    PRIMARY KEY(MemberID),
    FOREIGN KEY(MemberID) REFERENCES Member(MemberID)
    );"""
    
    #Creates a database connection.
    connection = CreateConnection(database)
    
    #Creates the tables.
    if connection is not None:
        CreateTable(connection, CreateMemberTable)
        CreateTable(connection, CreateStaffTable)
        CreateTable(connection, CreateAdminTable)
        CreateTable(connection, CreateFlights)
        CreateTable(connection, CreateFlightsBooked)
        CreateTable(connection, CreateDataTable)
    else:
    #If any problems occur, the error will be catches and suitable message will be outputed.
        print("An error occured, cannot establish database connection.")
        

def InsertMember(connection, Members):
    #Inserts a new member in the Members table.
    sql = """INSERT INTO Member(MemberID, Firstname, Surname, Email, MobileNumber, Hash, Salt)
    VALUES(?, ?, ?, ?, ?, ?, ?)"""

    #Creates the cursor object by calling the cursor() function method of the connection object.
    c = connection.cursor()
    #Executes to the as the sql statement passed in.
    c.execute(sql, Members)

def InsertStaff(connection, Staffs):
    #Inserts a new staff in the Staffs table.
    sql = """INSERT INTO Staff(StaffID, Firstname, Surname, Email, MobileNumber, Hash, Salt) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        
    c = connection.cursor()
    c.execute(sql, Staffs)

def InsertFlights(connection, Flights):
    #Inserts new flights Flights
    sql = """INSERT INTO Flights(FlightID, FlightName) VALUES(?, ?)"""
        
    c = connection.cursor()
    c.execute(sql, Flights)

def InsertFlightsBooked(connection, FlightsBooked):
    #Inserts flights booked into the InsertFlightsBooked table.
    sql = """INSERT INTO FlightsBooked(MemberID, FlightID) VALUES(?, ?)"""
        
    c = connection.cursor()
    c.execute(sql, FlightsBooked)

def deleteFlights(connection, FlightID):
    #Deletes the flights from the Flights table using FlightID.
    sql = "DELETE FROM Flights WHERE FlightID = ?"
    
    c = connection.cursor()
    c.execute(sql, (FlightID,))
    connection.commit()

def deleteFlightsBooked(connection, FlightID):

    sql = "DELETE FROM FlightsBooked WHERE FlightID = ?"

    c = connection.cursor()
    c.execute(sql, (FlightID,))
    connection.commit()

def deleteStaff(connection, StaffID):
    sql = "DELETE FROM Staff WHERE StaffID = ?"

    c = connection.cursor()
    c.execute(sql, (StaffID,))
    connection.commit()


def updateMember(connection, MemberUpdate):
    #Updates the member from the Member table.
    sql = """UPDATE Member SET Firstname = ?, Surname = ?, Email = ?, MobileNumber = ?, Hash = ?, Salt = ? WHERE MemberID = ?"""

    c = connection.cursor()
    c.execute(sql, MemberUpdate)
    connection.commit()

def updateStaff(connection, StaffUpdate):
    #Updates the staff from the Staff table.
    sql = """UPDATE Staff SET Firstname = ?, Surname = ?, Email = ?, MobileNumber = ?, Hash = ?, Salt = ? WHERE StaffID = ?"""

    c = connection.cursor()
    c.execute(sql, StaffUpdate)
    connection.commit()

def updateAdmin(connection, AdminUpdate):
    #Updates the admin from the admin table.
    sql = """UPDATE Admin SET Firstname = ?, Surname = ?, Email = ?, MobileNumber = ?, Hash = ?, Salt = ? WHERE AdminID = ?"""

    c = connection.cursor()
    c.execute(sql, AdminUpdate)
    connection.commit()

def insertDefaultMembers():
    database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
    connection = CreateConnection(database)

    #2-Dimensional array.
    members = (
        [

        #Amrith2001££
        ["3634", "Amrith", "Townsend", "amrith90434@gmail.com", "07984475737",
        "be9a148a9d25ce2a5334c4444d5c38205942e5d1bcb92fe52c1649f93e435374",
        "cbb5e743b4e00457f76ca894130a74c609a2e6bfe4a25e3c4b6f5b4b9eb16f27"],
        #Jeanne!!!!56
        ["9560", "Jeanne", "Graves", "jeanne1980@yahoo.com", "07712811567",
        "3eda3dad79f17ca4622e873f094d68d9b64536a63784986042b915ca19730969",
        "68534e365799d4434b18dba6d8fc1f8a054a965bd5c02d5a3addae7985b66423"],
        #ChaseMaguire1999$$
        ["7228", "Chase", "Maguire", "chasemaguire1999@gmail.com", "07465257285",
        "75cee604be8eecc2bd429ae727662db1561bb9c8ef89fe4332d8401c69148279",
        "2c0259b8f529f87bdb9add3e6b97d97a63a21a0b608a9b985fb8b62f4dca8d45"],
        #BertieLegge8944@@!
        ["8659", "Bertie", "Legge", "bertlegge@mail.com", "07452397183",
        "029048f2279561768a484f09e6f043f47ed8d964f55b43e0860852a61161730d",
        "88575830be9c8951cda78feffefe22be434cc862ce8e24c34536bbbd2968f8b0"],
        #CodingBlonde49854
        ["4854", "Marsha", "Rivers", "codingblonde@gmail.com", "07945026036",
        "45a4abba1bc8b08d00f729531f6d7ae96ec4b23834583630817554104de979fa",
        "9ec5c4bef6f2bb26c49f0c9ee8d2e118aa5d38727a547d71099167881d81367b"],
        #ILoveEconomics!3453
        ["1897", "Ella", "Rose", "elllarose8345@outlook.com", "07712811567",
        "2f230bc936add2723000a4a44dad2f7d375ae438b5b4452465d950140635daea",
        "bcb1faf695719909615d06150d39487a469b4a9d42920835a8e8a2cd08e2c525"],
        #Python@@££££
        ["6966", "Jena", "Crawford", "jenacraw45@yahoo.com", "07624889686",
        "d977641f4eaf90f692ec28a7e047bbdd2dd875cd3fe3db729dc4dcbe5dd80a72",
        "5a1b61ebdc2937c62ef2fb8cb6591f5d5e36bd80a17eb34fe37317fab17ad5cf"],
        #EisaSwift2wQ£$£$
        ["5875", "Eisa", "Kearney", "eisakearney2001@gmail.com", "07753570048",
        "4d5158c7ce4048d8eaafa8a1fb068babc382b44c323eb83da41146f92537a2d9",
        "b76686ca4e6aaa1e5d4d80ab29ee7b9894e6a785b42c96cc505cc7dce5c6ee9d"],
        #LeblancBlaine23q45w
        ["2465", "Blaine", "Leblanc", "l.blaine@gmail.com", "07808607682",
        "adc80e2d53968d4df5e6d6df0e9101b4004c83d43d14229c88639ff7080fba9b",
        "08332bef5277c7dc59637c6971e8353b121e50d135d6e6852bae422a6099157a"],
        #KathyPacific436QQQ
        ["0270", "Kathy", "Oslen", "o.kathy@outlook.com", "07873904823",
        "f3fb9a6fa9603e8efe168dc82cfc26801a313d67c066af3acd826884bf59e646",
        "1b27ea4084c3fd7850eef217e43a942c01cd360a4e79ad6685354a6d800f2010"],
        #Karla17QQQQ
        ["5443", "Karla", "Kelmp", "karlakelmp1999@yahoo.com", "07523765894",
        "57486e5e2516ada69bdb4e3237105b952e6cea453ba7d0fcb7beb98e6edb641b",
        "d7649e8924def89eaf85cfe8f417e549f007a20804669543c880333403b08794"],
        #Gailwwg1Wga
        ["6430", "Gail", "Rocha", "gailrocha1998@gmail.com", "07440446862",
        "f4f04dcc01df0b4e26c7b0616959c6c5205953e0d44f36c824fc66a9f4fdf335",
        "5a2ee7defbc6d47a420d14713b7f8a0a313f1e7fb0a09b488fcead6e02a8557b"]

        ]
        )

    for member in range(len(members)):
        with connection:
            member = (members[member])
            InsertMember(connection, member)

def insertDefaultStaffs():
    database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
    connection = CreateConnection(database)

    #2-Dimensional array.
    staffs = (
        [

        #Nikas8979@
        ["6573", "Nikas", "miles", "nikas@gmail.com", "07809989897",
        "427fe29c6c6846e6f3468335e7ae25b8ce05cc865eb7a285df237f29a66466e4",
        "9ad48b112757cb2c87039bf1d310a5487c1ca4586cd6cd49bef71a2367cf964c"],
        #Memz9285£
        ["8653", "Mehmet", "Schwartz", "mehmettmazi@yahoo.com", "074988767867",
        "36f33e5ac70dd4b48f9637e6a7a979cfaa20491af1c23de28cc2f67535a8aa3a",
        "b74141ce4c46023e78f684f2468de6fb44dea0b0161f573209c3c60f96dd4da5"],
        #BrandonBiba!!@
        ["5986", "Brandon", "Zamora", "brandino@mail.com", "07246678678",
        "30f0b72eb9a58063dd5749249cc305e7cf7f8f1ac66d1f5b5271461ca307a539",
        "6e350b313d0ce7e8e44e3485e7dfc21de1e34a08b439c8cdfa2a93691c003b9f"],
        #Okan5673£
        ["3490", "Okan", "Griffiths", "okaikan3457@gmail.com", "07809989897",
        "cb8291ca12715a2909bf55e8c767a64a64b03aa0ee812cf22f0bf93d70a1c958",
        "3d08dbb701450e7bf83246463e45aff2b9ca4f1e651c56ffabbcbef8f373d313"],
        #Sanjeevz3009@
        ["5689", "Sanjeev", "Nguyen", "sanjeevNguyen@gmail.com", "07809989897",
        "8c729f60085e102d317b5c1a176647cc8830cbb430ed00d250b348c8e631fac3",
        "edf10aa28d28ea2efe2096e2cb9947d30aa3720a26e19dcbe260a6eb1fc1c72e"]

        ]
        )

    for staff in range(len(staffs)):
        with connection:
            staff = (staffs[staff])
            InsertStaff(connection, staff)

def insertDefaultAdmins():
    database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
    connection = CreateConnection(database)

    #Admin1234@
    admin = ["8389", "Elliot", "Choy", "qjetbot1111@gmail.com", "07656656767",
    "a97e6879808e4cca83b581ef114eb51477bcb9aa803b4e7b828dae43b7997a83",
    "abb9b5f8051de99478e40ad8c4a1e5c53df4b6f0dac6c9543bcdf150652b2e28"]

    with connection:
        sql = """INSERT INTO Admin(AdminID, Firstname, Surname, Email, MobileNumber, Hash, Salt) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        
        c = connection.cursor()
        c.execute(sql, admin)


def insertDefaultFlights():
    database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
    connection = CreateConnection(database)

    #2-Dimensional array.
    flights = (
        [

        ["6790", "London Heathrow - Doha Qatar, £467.78"],
        ["5412", "Doha Qatar - London Heathrow, £483.46"],
        ["6426", "London Heathrow - Barcelona Spain, £109.56"],
        ["5624", "Barcelona Spain - London Heathrow, £111.11"],
        ["4879", "London Heathrow - Las Vegas USA, £400.71"],
        ["8494", "Las Vegas USA - London Heathrow, £390.89"],
        ["5214", "London Heathrow - New York USA, £280.96"],
        ["7152", "New York USA - London Heathrow, £270.24"],
        ["4663", "London Heathrow - San Francisco USA, £280.92"],
        ["6278", "San Francisco USA - London Heathrow, £279.21"],
        ["1755", "London Heathrow - Mauritius, £701.65"],
        ["8047", "Mauritius - London Heathrow, £710.23"],
        ["4451", "London Heathrow - Melbourne AUS, £751.88"],
        ["7802", "Melbourne AUS - London Heathrow, £730.95"],
        ["1111", "London Heathrow - Sydney AUS, £748.52"],
        ["2527", "Sydney AUS - London Heathrow, £711.67"],
        ["6588", "London Heathrow - Mexico City Mexico, £744.11"]
        
        ]
        )

    for flight in range(len(flights)):
        with connection:
            InsertFlights(connection, flights[flight])

def insertDefualtFlightData():
    database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
    connection = CreateConnection(database)

    #2-Dimensional array.
    memberData = (
        [

        ["9560", "9", "0"],
        ["7228", "16", "4"],
        ["8659", "17", "3"],
        ["4854", "6", "1"],
        ["1897", "13", "4"],
        ["6966", "12", "2"],
        ["5875", "7", "3"],
        ["2465", "16", "7"],
        ["0270", "4", "0"],
        ["5443", "8", "1"],
        ["6430", "18", "6"]
        
        ]
        )

    for data in range(len(memberData)):
        with connection:
            sql = """INSERT INTO Data(MemberID, BookedFlights, CancelledFlights) VALUES(?, ?, ?)"""
        
            c = connection.cursor()
            c.execute(sql, memberData[data])


def testSQL():
    database = r"C:\Users\Deadsec\Desktop\CS-NEA\QJet\Qjet\qjetdatabase.db"
    connection = CreateConnection(database)
    c = connection.cursor()

    c.execute("SELECT Firstname FROM Member")

    data = c.fetchall()
    print(data)
    firstName = []

    for firstname in data:
        for firstnameList in firstname:
            firstName.append(firstnameList)
    print(firstName)



if __name__ == "__main__":
    insertDefaultStaffs()