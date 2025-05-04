#***************************************************************
#
#  Function:     createLists
# 
#  Description:  This function reads the file and creates the lists
#                Please do NOT modify this function.  If you do,
#                you will not receive credit for Program 8.
#
#  Parameters:   The file objects
#
#  Returns:      The four lists 
#
#**************************************************************
def createLists(inFile, outFile):
    idList = []
    incomeList = []
    membersList = []
    statesList = []
	
    outFile.write(str("%12s     %-12s  %-8s  %-8s\n" % ("Account #", " Income", "Members", "State")))
    #print("%12s     %-12s  %-8s  %-8s\n" % ("Account #", " Income", "Members", "State"))
		
    lineRead = inFile.readline()       # Read first record
    while lineRead != '':              # While there are more records
       words = lineRead.split()        # Split the records into substrings
       idNum = int(words[0])           # Convert first substring to integer
       annualIncome = float(words[1])  # Convert second substring to float
       members = int(words[2])         # Convert third substring to integer
       states = words[3]
       
       #print("%10d  %12.2f  %8d     %-15s" % (idNum, annualIncome, members, states))
       outFile.write(str("%10d   %12.2f  %8d     %-15s\n" % (idNum, annualIncome, members, states)))

       idList.append(idNum)
       incomeList.append(annualIncome)
       membersList.append(members)
       statesList.append(states)

       lineRead = inFile.readline()    # Read next record
       
    # Close the input file.
    inFile.close() # Close file
    
    return idList, incomeList, membersList, statesList
    #End of the createLists function
