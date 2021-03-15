#Matplotlib is a comprehensive library for creating static,
#animated, and interactive visualizations in Python.
import matplotlib
import matplotlib.pyplot as plt
#NumPy is the fundamental package for scientific computing with Python
import numpy as np
#Use to generate spreadsheet files compatible with Microsoft Excel.
import xlwt
from xlwt import Workbook
#Importing my SQL database module.
from qjetdatabase import *

#dataSet class will contain the data related to number of members, booked flights
#and cancelled flights.
class dataSet(object):
    #Constructor is made, __init__() function to assign values to object properties or
    #other operations that are necessaeay to do when the objects is being created.
    #The __init__() function is called automatically every time the class is 
    #being used to create a new object.

    #The self parameter is a reference to the current instance of the class,
    #and is used to access variables that belong to the class.
	def __init__(self, numMember, numBookedFlights, numCancelledFlights):
		#Assigning values to object properties.
		self.numMember = numMember
		self.numBookedFlights = numBookedFlights
		self.numCancelledFlights = numCancelledFlights

#This showGroupedBarGraph class will execute and perform the operations necessary to show a,
#a grouped bar graph.
#showGroupedBarGraph will inherit from the dataSet class.
#It can be called a child class of the dataSet class.	
class showGroupedBarGraph(dataSet):
	def __init__(self, numMember, numBookedFlights, numCancelledFlights):
		#super() function will make the child class inherit all the methods,
		#and properties from its parent. In this case from dataSet.
		super().__init__(numMember, numBookedFlights, numCancelledFlights)

	#The method outputCheck contains the algorithms and executes the operations,
	#necessary to output a grouped bar graph. 
	def outputCheck(self):
		print("MemberID", self.numMember)
		print("Booked flights", self.numBookedFlights)
		print("Cancelled flights", self.numCancelledFlights)

		#Number of the booked flights instance variable will be assigned to the, variable
		#called listNum. A overiding will take place at this point.
		listNum = self.numBookedFlights
		#The mergeSort class will be instatiated here and 3 parameters are passed on,
		#as instance variables.
		a = mergeSort(self.numMember, self.numBookedFlights, self.numCancelledFlights)
		#The mergeSortFunction method from the mergeSort class will be executed taking listNum as a parameter.
		a.mergeSortFunction(listNum)
		#The new sorted list of numbers using my merge sort algorithm will be assinged to the,
		#variable sortedBookedFlights.
		sortedBookedFlights = listNum
		
		#Number of cancelled flights instance variable wil be assgined to the variable,
		#listNum.
		listNum = self.numCancelledFlights
		#mergeSort class is instantiated here and 3 parameters are passed on, as
		#instance variables.
		a = mergeSort(self.numMember, self.numBookedFlights, self.numCancelledFlights)
		#mergeSortFunction method from the mergeSort class will be executed.
		a.mergeSortFunction(listNum)
		#The sorted list of numbers that was sorted using the mergeSort algirthm will be assigned,
		#to the variable sortedCancelledFlights.
		sortedCancelledFlights = listNum

		print("sortedBookedFlights", sortedBookedFlights)
		print("sortedCancelledFlights", sortedCancelledFlights)

		#The labels of x and y axis are set. 
		labels = self.numMember
		#bookedFlights will be the sorted list of numbers of booked flights.
		bookedFlights = sortedBookedFlights
		#cancelledFlights will be the sorted list of numbers of cancelled flights.
		cancelledFlights = sortedCancelledFlights

		#The label locations
		x = np.arange(len(labels))  
		#The width of the bars
		width = 0.4  

		#The graph plotting is executed.
		fig, ax = plt.subplots()
		#Booked flights list of numbers are plotted.
		rects1 = ax.bar(x - width/2, bookedFlights, width, label='Booked', color = "green")
		#Cancelled flights list of numbers are plotted here.
		rects2 = ax.bar(x + width/2, cancelledFlights, width, label='Cancelled', color = "red")

		#Add some text for labels, title and custom x-axis tick labels, etc.
		ax.set_ylabel('Number of flights')
		ax.set_title('Booked and cancelled flights')
		ax.set_xticks(x)
		ax.set_xticklabels(labels)
		ax.legend()

		def autolabel(rects):
		    """Attach a text label above each bar in *rects*, displaying its height."""
		    for rect in rects:
		        height = rect.get_height()
		        ax.annotate('{}'.format(height),
		                    xy=(rect.get_x() + rect.get_width() / 2, height),
		                    xytext=(0, 3),  # 3 points vertical offset
		                    textcoords="offset points",
		                    ha='center', va='bottom')

		autolabel(rects1)
		autolabel(rects2)

		fig.tight_layout()

		#Finally the group bar graph will be shown to the user.
		plt.show()

#This pieChart class will execute and perform the operations necessary to show a, pieChart.
#pieChart will inherit from the showGroupedBarGraph class.
#It can be called a child class of the showGroupedBarGraph class.
class pieChart(showGroupedBarGraph):
	#super() function will make the child class inherit all the methods,
	#and properties from its parent. In this case from showGroupedBarGraph.
	def __init__(self, numMember, numBookedFlights, numCancelledFlights):
		super().__init__(numMember, numBookedFlights, numCancelledFlights)

	#The method outputCheck contains the algorithms and executes the operations,
	#necessary to output a pie chart. 	
	def outputCheck(self):
		print("MemberID", self.numMember)
		print("Booked flights", self.numBookedFlights)
		print("Cancelled flights", self.numCancelledFlights)

		#Number of the booked flights instance variable will be assigned to the, variable
		#called listNum. A overiding will take place at this point.
		listNum = self.numBookedFlights
		#The mergeSort class will be instatiated here and 3 parameters are passed on,
		#as instance variables.
		a = mergeSort(self.numMember, self.numBookedFlights, self.numCancelledFlights)
		#The mergeSortFunction method from the mergeSort class will be executed taking listNum as a parameter.
		a.mergeSortFunction(listNum)
		#The new sorted list of numbers using my merge sort algorithm will be assinged to the,
		#variable sortedBookedFlights.
		sortedBookedFlights = listNum
		
		#All the numbers will be added from the sortedBookedFlights list.
		sumBookedFlights = sum(sortedBookedFlights)

		#Number of cancelled flights instance variable wil be assgined to the variable,
		#listNum.
		listNum = self.numCancelledFlights
		#mergeSort class is instantiated here and 3 parameters are passed on, as
		#instance variables.
		a = mergeSort(self.numMember, self.numBookedFlights, self.numCancelledFlights)
		#mergeSortFunction method from the mergeSort class will be executed.
		a.mergeSortFunction(listNum)
		#The sorted list of numbers that was sorted using the mergeSort algirthm will be assigned,
		#to the variable sortedCancelledFlights.
		sortedCancelledFlights = listNum

		#All the numbers will be added from the sumCancelledFlights list.
		sumCancelledFlights = sum(sortedCancelledFlights)

		print("sortedBookedFlights", sortedBookedFlights)
		print("sortedCancelledFlights", sortedCancelledFlights)

		print("sumBookedFlights", sumBookedFlights)
		print("sumCancelledFlights", sumCancelledFlights)

		#Pie chart, where the slices will be ordered and plotted counter-clockwise:
		labels = 'Booked flights', 'Cancelled flights'
		sizes = sumBookedFlights, sumCancelledFlights
		explode = (0, 0.08)  # only "explode" the 2nd slice (i.e. 'Hogs')

		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1f%%',
		        shadow=True, startangle=90)
		ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

		#Finally the pie chart will be shown to the user.
		plt.show()

#This mergeSort class will execute and perform the operations necessary to sort all,
#the numbers in a list from lowest to highest order.
#mergeSort will inherit from the pieChart class.
#It can be called a child class of the pieChart class.
class mergeSort(pieChart):
	def __init__(self, numMember, numBookedFlights, numCancelledFlights):
		#super() function will make the child class inherit all the methods,
		#and properties from its parent. In this case from pieChart.
		super().__init__(numMember, numBookedFlights, numCancelledFlights)

	#mergeSortFunction will peform all the executions and operations necessary,
	#to sorrt the list of numbers inputted as a parameter, in this case listNum,
	#parameter takes in a list of numbers. 
	def mergeSortFunction(self, listNum):
		if len(listNum) > 1:
			print("Length of the input list: ", str(len(listNum)) + "\n")

			#Finds the middle of the array .
			middleValue = len(listNum)//2 
			print("Middle value of the list", str(middleValue) + "\n")

			#Dividing the array elements into two halves.
			leftSide = listNum[:middleValue] 
			print("Current left side of the list:", leftSide)

			rightSide = listNum[middleValue:] 
			print("Current right side of the list:", rightSide)
			
			#Sorting the first half of the list given.
			self.mergeSortFunction(leftSide)
			print("Merge sort function left side: ", str(leftSide) + "\n")

			#Sorting the second half of the list given.
			self.mergeSortFunction(rightSide) 
			print("Merge sort function right side: ", str(rightSide) + "\n")
	  
			i = 0
			j = 0 
			k = 0 
			print("Current i j k values: ", i, j, k)
			  
			#Copy data to temporary lists leftSide[] and rightSide[]. 
			#While 0 is < length of leftSide list and 0 is < length of rightSide list, keep running.
			while i < len(leftSide) and j < len(rightSide): 
				#If leftSide list position 0 element is < rightSide list position 0 element listNum position 0 element equal to
				#leftSide list positon 0 element.
				#E.g. If 5 is < 4 listNum list index position 0 element will be set to leftSide index posotion 0 element
				#which is 4. So first element in the listNum will be 4.
				if leftSide[i] < rightSide[j]:
					listNum[k] = leftSide[i]
					print("Current1 listNum list: ", listNum) 
					#i will be added by 1.
					i+=1
				else: 
					#Or if leftSide index position 0 element is not < rightSide index position 0 element.
					#listNum index position 0 element will be set to rightSide index position 0 element.
					listNum[k] = rightSide[j] 
					print("Current2 listNum list: ", listNum)
					#j is added by 1.
					j+=1
				#k is added by 1.
				k+=1
			  
			#Checking if any list element was left out.
			while i < len(leftSide): 
				listNum[k] = leftSide[i] 
				print("Current3 listNum list: ", listNum)
				i+=1
				k+=1
			  
			while j < len(rightSide): 
				listNum[k] = rightSide[j] 
				print("Current4 listNum list: ", listNum)
				j+=1
				k+=1

#This exportToTextAndExcel class will execute and perform the operations necessary to,
#export data such as booked flights, cancelled flights, total booked and cancelled flights,
#to an excel and text file.
#exportToTextAndExcel will inherit from the dataSet class.
#It can be called a child class of the dataSet class.
class exportToTextAndExcel(dataSet):
	def __init__(self, numMember, numBookedFlights, numCancelledFlights, totalMembers):
		#super() function will make the child class inherit all the methods,
		#and properties from its parent. In this case from dataSet.
		super().__init__(numMember, numBookedFlights, numCancelledFlights)
		#totalMembers attribute will be assigned to the instance variable self.totalMembers,
		#so it can be referenced later on in the program.
		self.totalMembers = totalMembers

	#exportToText method will export the needed data to a text file.
	def exportToText(self):
		#Using the function sum, the numBookedFlights list numbers will be added together,
		#and this will be stored in the totalBookedFlights variable.
		totalBookedFlights = sum(self.numBookedFlights)
		#Using the function sum, the numCancelledFlights list numbers will be added together,
		#and this will be stored in the totalCancelledFlights variable.
		totalCancelledFlights = sum(self.numCancelledFlights)

		#with open is used, so the text file will be closed automatically once,
		#the operations are completed such as file writes, preventing any changes being,
		#made accidently. 
		with open("qjetBusinessData.txt", "w") as file:
			file.write("Qjet business data: " + "\n" + "====================" + "\n" + "\n")

			#A for loop is run until the duration of the length of the numMember list.
			for i in range(len(self.numMember)):
				#All the memberID, booked flights and cancelled flights will be written,
				#to the text file.
				file.write("MemberID: " + self.numMember[i] + ", " 
					+ "Booked flights:" + str(self.numBookedFlights[i]) + ", " 
					+ "Cancelled flights: " +  str(self.numCancelledFlights[i]) + 
					"\n" + "\n")

			file.write("Summary:" + "\n" + "=========" + "\n")

			#The total booked and cancelled flights will be written to the text file.
			file.write("Total members: " + str(self.totalMembers) + ", " 
				+ "Total booked flights: " + str(totalBookedFlights) + ", " 
				+ "Total cancelled flights: " + str(totalCancelledFlights))

	#exportToExcel method will export the needed data to a excel spreadsheet.
	def exportToExcel(self):
		#Workbook is created.
		wb = Workbook()

		#Applying multiple styles , such as colours.
		style = xlwt.easyxf('font: bold 1, color green;') 
		style2 = xlwt.easyxf('font: bold 1, color red;') 


		#Add sheet is used to create a excel spread sheet.
		sheet1 = wb.add_sheet("Sheet1")

		#The column names are written to the excel file. 
		sheet1.write(0, 1, 'MemberIDs') 
		sheet1.write(0, 2, 'Booked flights', style) 
		sheet1.write(0, 3, 'Cancelled flights', style2) 

		#The row name is written to the excel file.
		sheet1.write(14, 0, "Total", style)

		#The total members, booked and cancelled flight numbers are,
		#are written to the excel file.
		sheet1.write(14, 1, self.totalMembers)
		sheet1.write(14, 2, sum(self.numBookedFlights))
		sheet1.write(14, 3, sum(self.numCancelledFlights))

		#A for loop is executed until the length of the numMember list.
		for memberID in range(len(self.numMember)):
			#The memberIDs are written to the excel file.
			sheet1.write(memberID + 1, 1, self.numMember[memberID])

		#A for loop is run until the length of the numBookedFlights list.
		for bookedFlights in range(len(self.numBookedFlights)):
			#The booked flights data will be written to the excel file.
			sheet1.write(bookedFlights + 1, 2, self.numBookedFlights[bookedFlights])

		#For loop is run until the length of the numCancelledFlights list.
		for cancelledFlights in range(len(self.numCancelledFlights)):
			#The cancelled flights data will be written to the excel file.
			sheet1.write(cancelledFlights + 1, 3, self.numCancelledFlights[cancelledFlights])
		
		#The excel file will be saved and outputted to the current directory.	
		wb.save("qjetBusinessData.xls")

#The start class is used by the other modules in the program where, if the user wants to,
#export data to text and excel or view a particular data graph this class will need to be instantiated first.
#Then a class method will be executed which will run the other classes if needed.		
class start(object):
	def __init__(self):
		#Database location is specified.
		database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
		#Using my qjetdatabase module, CreateConnection function is called and the,
		#database connection is established.
		connection = CreateConnection(database)
		#Curson object is defined.
		c = connection.cursor()

		#SQL SELECT statement is run the query for the MemberIDs from the Data table.
		c.execute("SELECT MemberID FROM Data")
		data = c.fetchall()
		print(data)

		#A list comprehension is performed to convert the data from 2D array/ list to,
		#1D array/ list to work with.
		#A for loop is used for this.
		self.numMember = []
		for memberIDs in data:
			for memberID in memberIDs:
				#Member IDs are appeneded to the numMember list.
				self.numMember.append(memberID)

		#SQL SELECT statement is run the query for the BookedFlights from the Data table.
		c.execute("SELECT BookedFlights FROM Data")
		data = c.fetchall()
		print(data)

		#A list comprehension is performed to convert the data from 2D array/ list to,
		#1D array/ list to work with.
		#A for loop is used for this.
		self.numBookedFlights = []
		for bookedFlights in data:
			for bookedFlight in bookedFlights:
				#Number of booked flights is appended to the numBookedFlights list.
				self.numBookedFlights.append(bookedFlight)

		#SQL SELECT statement is run the query for the CancelledFlights from the Data table.
		c.execute("SELECT CancelledFlights FROM Data")
		data = c.fetchall()
		print(data)

		#A list comprehension is performed to convert the data from 2D array/ list to,
		#1D array/ list to work with.
		#A for loop is used for this.
		self.numCancelledFlights = []
		for cancelledFlights in data:
			for cancelledFlight in cancelledFlights:
				#Number of cancelled flights is appended to the numCancelledFlights list.
				self.numCancelledFlights.append(cancelledFlight)

		self.totalMembers = 0 
		#A for loop run until the length of the numMember list to work out how many members are in the,
		#member table to calculate the total number of memebrs who are registered with Qjet.
		for i in range(len(self.numMember)): self.totalMembers += 1

	#showPieChart method is executed from other modules so, a pie chart can be shown to the user.
	def showPieChart(self):
		sendData = pieChart(self.numMember, self.numBookedFlights, self.numCancelledFlights)
		#The data necessary to draw a pie chart will be sent to the pieChart class methods.
		sendData.outputCheck()

	#showGroupedBarGraph method is executed from other modules so, a pie chart can be shown to the user.
	def showGroupedBarGraph(self):
		sendData = showGroupedBarGraph(self.numMember, self.numBookedFlights, self.numCancelledFlights)
		#The data necessary to draw a pie chart will be sent to the showGroupedBarGraph class methods.
		sendData.outputCheck()

	#exportToText method is executed from other modules so, a a text file can be created/ written.
	def exportToText(self):
		sendData = exportToTextAndExcel(self.numMember, self.numBookedFlights, self.numCancelledFlights, self.totalMembers)
		#The data necessary to write the create/ write the text file will be sent to the exportToTextAndExcel class methods.
		sendData.exportToText()

	#exportToText method is executed from other modules so, a a excel file can be created/ written.
	def exportToExcel(self):
		sendData = exportToTextAndExcel(self.numMember, self.numBookedFlights, self.numCancelledFlights, self.totalMembers)
		#The data necessary to write the create/ write the excel file will be sent to the exportToTextAndExcel class methods.
		sendData.exportToExcel()



	





