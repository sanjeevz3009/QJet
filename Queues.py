# Python program to 
# demonstrate implementation of 
# queue using queue module 
from queue import Queue 
from qjetdatabase import *

database = r"C:\Users\Deadsec\Desktop\QJet\Qjet\qjetdatabase.db"
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

lengthList = len(firstName)

# Initializing a queue 
q = Queue(maxsize = lengthList) 
  
# qsize() give the maxsize  
# of the Queue  
print(q.qsize())  
  
# Adding of element to queue

for i in range(lengthList):
	q.put(firstName[i]) 
	
  
# Return Boolean for Full  
# Queue  
print("\nFull: ", q.full())  
  
# Removing element from queue 
print("\nElements dequeued from the queue") 
print(q.get()) 
print(q.get()) 
print(q.get()) 
  
# Return Boolean for Empty  
# Queue  
print("\nEmpty: ", q.empty()) 
  
q.put(1) 
print("\nEmpty: ", q.empty())  
print("Full: ", q.full()) 
  
# This would result into Infinite  
# Loop as the Queue is empty.  
# print(q.get()) 