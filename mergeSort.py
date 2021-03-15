import random

def mergeSortFunction(listNum): 
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
        mergeSortFunction(leftSide)
        print("Merge sort function left side: ", str(leftSide) + "\n")

        #Sorting the second half of the list given.
        mergeSortFunction(rightSide) 
        print("Merge sort function right side: ", str(rightSide) + "\n")
  
        i = 0
        j = 0 
        k = 0 
        print("Curren i j k values: ", i, j, k)
          
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
  
listNum = [5, 8, 0, 4, 7, 2]

mergeSortFunction(listNum)
print(listNum)

  