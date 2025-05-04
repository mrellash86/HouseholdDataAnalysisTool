#********************************************************************
#
#  Developer:    Ell Ash
#
#
#  Description:  A program that reads survey results from 'Program8.txt'
#                into lists using the CreateLists module, performs
#                data analysis including average income, identifying
#                households above average, below poverty, and potentially
#                eligible for Medicaid, and writes the results to
#                'Program8-Output.txt'. Follows specific function
#                structure and constraints.
#
#                Do not modify the main method or the header of any
#                method. You will not receive credit for Program 8
#                if you do. 
#
#********************************************************************

# Import the required module to create the lists from the input file
import CreateLists 

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main method of the program. Orchestrates file
#                opening, data loading via CreateLists, calling
#                analysis functions, and ensures output is written.
#                (Requirement: No input, processing, or output here,
#                 delegate work).
#                Do NOT modify this method. If you modify it, you
#                will not receive credit for this program.
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():

    # Open the input file 'Program8.txt' for reading ('r')
    inFileObject  = open('Program8.txt', 'r') 
    # Open the output file 'Program8-Output.txt' for writing ('w')
    # (Requirement: Output should be sent to Program8-Output.txt)
    outFileObject = open('Program8-Output.txt', 'w') 

    # Call function to write developer information to the output file
    # (Requirement: Have at least six functions, developerInfo included)
    developerInfo(outFileObject) 
    
    # Call the function from the CreateLists module.
    # This function is expected to:
    # 1. Read data from inFileObject (Program8.txt).
    # 2. Print the initial household records (Requirement a - completed in CreateLists).
    # 3. Return the four parallel lists: ids, incomes, members, states.
    idList, incomeList, membersList, statesList = \
            CreateLists.createLists(inFileObject, outFileObject) 

    # Call function to calculate the average income (Requirement b - calculation part)
    # (Requirement: Delegate work to other functions)
    average = calcAverageIncome(incomeList) 
    
    # Call function to print the average income and list households above average
    # (Requirement b - printing part)
    # (Requirement c - list households above average)
    # (Requirement: Delegate work to other functions)
    findIncomeAboveAverage(outFileObject, average, idList, incomeList, membersList, statesList) 
    
    # Call function to find households below poverty level and calculate/print percentage
    # (Requirement d - list households below poverty)
    # (Requirement e - calculate and print percentage below poverty)
    # (Requirement: Delegate work to other functions)
    findIncomeBelowPovertyLevel(outFileObject, idList, incomeList, membersList, statesList) 
    
    # Call function to find households potentially qualifying for Medicaid and calculate/print percentage
    # (Requirement f - calculate and print percentage qualifying for Medicaid)
    # (Requirement: Delegate work to other functions)
    findQualifyForMedicaid(outFileObject, idList, incomeList, membersList, statesList) 
    
    # Close the input file object - good practice, though less critical for read-only
    inFileObject.close()
    # Close the output file object to ensure all data is written to disk
    outFileObject.close()
    
    # Inform the user on the console that the program finished and where output is
    print("Program processing complete. Output written to Program8-Output.txt")
    
    # End of the main function
    

#***************************************************************
#
#  Function:     calcAverageIncome
# 
#  Description:  Calculates the average household income from a list.
#                (Requirement b - calculation part).
#
#  Parameters:   income (list): A list of household incomes (floats/ints).
#
#  Returns:      float: The average income, or 0.0 if the list is empty.
#
#**************************************************************
def calcAverageIncome(income):
    # Get the total number of households (length of the income list)
    num_households = len(income) 
    
    # Check if the list is empty to prevent division by zero error
    if num_households == 0: 
        # Return 0.0 if there are no households to average
        return 0.0 
    
    # Calculate the sum of all incomes in the list
    total_income = sum(income) 
    
    # Calculate the average income by dividing the total by the number of households
    average = total_income / num_households 
    
    # Return the calculated average income
    return average 

    # End of calcAverageIncome function


#***************************************************************
#
#  Function:     findIncomeAboveAverage
# 
#  Description:  Prints the calculated average income to the output file,
#                then lists the details of households whose income is
#                strictly greater than the average.
#                (Requirement b - printing average income)
#                (Requirement c - listing households above average)
#
#  Parameters:   outFileObject: An open file object for writing output.
#                average (float): The calculated average household income.
#                idNum (list): List of household identification numbers.
#                income (list): List of household incomes.
#                members (list): List of household members.
#                state (list): List of household states.
#
#  Returns:      Nothing 
#
#**************************************************************
def findIncomeAboveAverage(outFileObject, average, idNum, income, members, state):
    # Write the calculated average income to the output file, formatted as currency
    # (Requirement b - print average income)
    outFileObject.write(f'Average Household Income: ${average:,.2f}\n\n') 

    # Write the header for the section listing households above average income
    # (Requirement c - provide headings)
    outFileObject.write('Households Above Average Income\n') 
    # Write a separator line under the header
    outFileObject.write("-" * 60 + "\n") 
    # Write the column headers, formatted for alignment
    # (Requirement c - four-column format with headings: ID, Income, Members, State)
    outFileObject.write(f"{'ID':<10}{'Income':<15}{'Members':<10}{'State':<10}\n") 
    # Write another separator line below the column headers
    outFileObject.write("-" * 60 + "\n") 

    # Initialize a counter for households found above average (optional, but good practice)
    count_above = 0 
    
    # Iterate through the lists using an index, assuming all lists have the same length
    for i in range(len(idNum)): 
        # Check if the income of the current household is greater than the average
        # (Requirement c - identify households that exceed the average)
        if income[i] > average: 
            # If above average, write the household's details to the output file
            # Format: ID (left-aligned, 10 spaces), Income (left-aligned, 15 spaces, comma sep, 2 decimals),
            # Members (left-aligned, 10 spaces), State (left-aligned, 10 spaces)
            # (Requirement c - print ID, income, members, state in four-column format)
            outFileObject.write(f"{idNum[i]:<10}{income[i]:<15,.2f}{members[i]:<10}{state[i]:<10}\n") 
            # Increment the counter
            count_above += 1 

    # If no households were found above average, write a message indicating that
    if count_above == 0:
        outFileObject.write("No households found above the average income.\n")

    # Write a final separator line and add vertical space for readability
    outFileObject.write("-" * 60 + "\n\n") 

    # End of findIncomeAboveAverage function


#***************************************************************
#
#  Function:     calcPovertyLevel
# 
#  Description:  Calculates the Federal Poverty Level (FPL) for a
#                single household based on the number of members and the state.
#                Uses the specific formulas provided in the assignment.
#                (Requirement: Compute poverty level using one of the formulas)
#
#  Parameters:   members (int): The number of members in the household.
#                state (str): The state abbreviation ('AK', 'HI', or other).
#
#  Returns:      float: The calculated poverty level income.
#
#**************************************************************
def calcPovertyLevel(members, state):
    # Assign the number of members to 'm' for use in the formulas
    m = members 

    # Handle cases where m might be less than 1 (e.g., data error) - assume at least 1 person
    if m <= 0:
        m = 1 # Ensure m is at least 1 for calculation logic

    # Calculate the term (m - 2), ensuring it's not negative for the multiplication part
    # This simplifies the formula application for m=1 or m=2 as well.
    members_factor = max(0, m - 2) 

    # Check if the state is Alaska ('AK')
    # (Requirement: Use formula for Alaska if state is AK)
    if state == 'AK': 
        # Calculate poverty level using the Alaska formula
        poverty_level = 25540.00 + 6730.00 * members_factor 
    # Check if the state is Hawaii ('HI')
    # (Requirement: Use formula for Hawaii if state is HI)
    elif state == 'HI': 
        # Calculate poverty level using the Hawaii formula
        poverty_level = 23500.00 + 6190.00 * members_factor 
    # Otherwise, assume it's one of the 48 contiguous states or DC
    # (Requirement: Use formula for 48 contiguous states/DC otherwise)
    else: 
        # Calculate poverty level using the formula for the 48 states/DC
        poverty_level = 20440.00 + 5380.00 * members_factor 

    # Return the calculated poverty level
    return poverty_level 

    # End of calcPovertyLevel function


#***************************************************************
#
#  Function:     findIncomeBelowPovertyLevel
# 
#  Description:  Identifies households with income below the calculated
#                Federal Poverty Level (FPL), prints their details
#                (including the calculated FPL), and then calculates and
#                prints the percentage of all households that fall below FPL.
#                (Requirement d - determine and print households below FPL)
#                (Requirement e - determine and print percentage below FPL)
#
#  Parameters:   outFileObject: An open file object for writing output.
#                idNum (list): List of household identification numbers.
#                income (list): List of household incomes.
#                members (list): List of household members.
#                state (list): List of household states.
#
#  Returns:      Nothing 
#
#**************************************************************
def findIncomeBelowPovertyLevel(outFileObject, idNum, income, members, state):
    # Write the header for the section listing households below poverty level
    # (Requirement d - provide headings)
    outFileObject.write("Households Below Federal Poverty Level (FPL)\n") 
    # Write a separator line
    outFileObject.write("-" * 70 + "\n") 
    # Write the column headers for the five columns
    # (Requirement d - five-column format: ID, Income, Poverty Level, Members, State)
    outFileObject.write(f"{'ID':<10}{'Income':<15}{'Poverty Lvl':<15}{'Members':<10}{'State':<10}\n") 
    # Write another separator line
    outFileObject.write("-" * 70 + "\n") 

    # Initialize a counter for households found below the poverty level
    # (Requirement e - needed to calculate percentage)
    count_below_poverty = 0 
    # Get the total number of households for percentage calculation
    total_households = len(idNum) 

    # Iterate through the lists using an index
    for i in range(total_households): 
        # Calculate the poverty level for the current household using the helper function
        # (Requirement d - determine poverty level for each household)
        poverty_level = calcPovertyLevel(members[i], state[i]) 

        # Check if the household's income is strictly less than their calculated poverty level
        # (Requirement d - identify households with income below FPL)
        if income[i] < poverty_level: 
            # If below poverty, write the household's details to the output file
            # Format: ID, Income, Poverty Level (formatted), Members, State
            # (Requirement d - print ID, income, poverty level, members, state)
            outFileObject.write(f"{idNum[i]:<10}{income[i]:<15,.2f}{poverty_level:<15,.2f}{members[i]:<10}{state[i]:<10}\n") 
            # Increment the counter for below-poverty households
            count_below_poverty += 1 

    # If no households were found below poverty, write a message indicating that
    if count_below_poverty == 0 and total_households > 0:
        outFileObject.write("No households found below the poverty level.\n")
    elif total_households == 0:
         outFileObject.write("No household data available to analyze.\n")

    # Write a separator line after the list
    outFileObject.write("-" * 70 + "\n\n") 

    # --- Calculate and Print Percentage Below Poverty (Requirement e) ---
    
    # Initialize percentage
    percentage_below_poverty = 0.0
    # Calculate the percentage only if there are households to avoid division by zero
    if total_households > 0:
        # Calculate percentage: (count below / total) * 100
        percentage_below_poverty = (count_below_poverty / total_households) * 100 

    # Write the header for the percentage result
    # (Requirement e - determine and print percentage)
    outFileObject.write("Percentage of Households Below Poverty Level\n") 
    # Write a separator line
    outFileObject.write("-" * 45 + "\n") 
    # Write the calculated percentage, formatted to two decimal places with a '%' sign
    outFileObject.write(f"{percentage_below_poverty:.2f}%\n") 
    # Write a final separator line and add vertical space
    outFileObject.write("-" * 45 + "\n\n") 

    # End of findIncomeBelowPovertyLevel function
    

#***************************************************************
#
#  Function:     findQualifyForMedicaid
# 
#  Description:  Determines the percentage of households that would
#                potentially qualify for Medicaid, assuming eligibility
#                is defined as having an income less than 138% of the
#                Federal Poverty Level (FPL). Prints this percentage.
#                (Requirement f - determine and print percentage for Medicaid)
#
#  Parameters:   outFileObject: An open file object for writing output.
#                idNum (list): List of household identification numbers.
#                income (list): List of household incomes.
#                members (list): List of household members.
#                state (list): List of household states.
#
#  Returns:      Nothing 
#
#**************************************************************
def findQualifyForMedicaid(outFileObject, idNum, income, members, state):
    # Define the Medicaid eligibility factor (138%)
    # (Requirement f - use 138% of FPL for Medicaid eligibility)
    MEDICAID_FACTOR = 1.38 

    # Initialize a counter for households potentially eligible for Medicaid
    count_medicaid_eligible = 0 
    # Get the total number of households for percentage calculation
    total_households = len(idNum) 

    # Iterate through the lists using an index
    for i in range(total_households): 
        # Calculate the poverty level for the current household using the helper function
        # (Requirement f - needs FPL to calculate 138% threshold)
        poverty_level = calcPovertyLevel(members[i], state[i]) 
        
        # Calculate the Medicaid income threshold (138% of the FPL)
        # (Requirement f - calculate 138% of FPL)
        medicaid_threshold = poverty_level * MEDICAID_FACTOR 

        # Check if the household's income is strictly less than the Medicaid threshold
        # (Requirement f - identify households below the 138% threshold)
        if income[i] < medicaid_threshold: 
            # Increment the counter if the household qualifies
            count_medicaid_eligible += 1 

    # --- Calculate and Print Percentage Qualifying for Medicaid (Requirement f) ---

    # Initialize percentage
    percentage_medicaid_eligible = 0.0
    # Calculate the percentage only if there are households to avoid division by zero
    if total_households > 0: 
        # Calculate percentage: (count eligible / total) * 100
        percentage_medicaid_eligible = (count_medicaid_eligible / total_households) * 100 

    # Write the header for the Medicaid qualification percentage result
    # (Requirement f - print the percentage)
    outFileObject.write("Percentage of Households Potentially Qualifying for Medicaid (Income < 138% FPL)\n") 
    # Write a separator line
    outFileObject.write("-" * 75 + "\n") 
    # Write the calculated percentage, formatted to two decimal places with a '%' sign
    outFileObject.write(f"{percentage_medicaid_eligible:.2f}%\n") 
    # Write a final separator line and add vertical space
    outFileObject.write("-" * 75 + "\n\n") 

    # End of findQualifyForMedicaid function


#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information (Name, Course, Program #, Due Date)
#                to the specified output file object.
#                (Requirement: Have at least six functions, developerInfo included)
#
#  Parameters:   outFileObject: An open file object for writing output.
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo(outFileObject):
    # Write programmer's name to the output file
    outFileObject.write('Name:     <Put your full name here>\n') # Replace with your actual full name
    # Write the course name to the output file
    outFileObject.write('Course:   Programming Fundamentals I\n') 
    # Write the program number to the output file
    outFileObject.write('Program:  Eight\n') 
    # Write the due date to the output file
    outFileObject.write('Due Date: <Due Date>\n\n') # Replace with the actual due date
    # End of the developerInfo function


# Call the main function if this script is executed directly.
# (Standard Python practice to ensure main() runs only when the script is the main program)
if __name__ == '__main__':
   # Execute the main function to start the program
   main() 
