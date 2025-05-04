# HouseholdDataAnalysisTool

Household Data Analysis Tool
This repository contains a Python program designed to process and analyze household survey data. The program reads structured data from an input file, organizes it into parallel lists, performs various analyses, and writes the results to an output file. The project is modular, adhering to clean coding principles by delegating specific tasks to individual functions.
________________________________________
Key Components
1. CreateLists.py
•	Purpose: A utility module that reads the input file and organizes the data into four parallel lists: account IDs, annual incomes, household members, and states.
•	Functionality:
o	Reads and processes each line of the input file.
o	Converts raw data into appropriate types (int, float, str).
o	Writes a formatted table of the raw data to the output file.
o	Returns the four lists for further analysis.
•	Output: A neatly formatted table summarizing the input data.
2. IncomeAndPovertyAnalysisTool.py
•	Purpose: The main program that orchestrates the workflow, performs data analysis, and generates the final report.
•	Functionality:
o	Reads survey data using the CreateLists module.
o	Calculates:
  	Average income.
  	Households above the average income.
  	Households below the poverty level and their percentage.
   	Households potentially qualifying for Medicaid and their percentage.
o	Writes all results to the output file.
•	Output: A comprehensive report summarizing the analysis.
________________________________________
Workflow
1.	Input: The program reads data from an input file (e.g., Program8.txt or a renamed equivalent).
2.	Data Preprocessing: The CreateLists module processes the data and returns structured lists.
3.	Analysis: The main program performs calculations and generates insights based on the data.
4.	Output: Results are written to an output file (e.g., Program8-Output.txt or a renamed equivalent).
________________________________________
How to Use
1.	Place the input file (e.g., Program8.txt) in the same directory as the program.
2.	Run the main program (IncomeAndPovertyAnalysisTool.py).
3.	The output file (e.g., Program8-Output.txt) will be generated with the results.
________________________________________
Technical Highlights
•	Modular Design: Functions are compartmentalized for readability and reusability.
•	File Handling: Ensures proper opening and closing of files to maintain resource integrity.
•	Data Validation: Converts raw input into appropriate data types for accurate analysis.
•	Formatted Output: Generates human-readable tables and reports.
This program is a robust tool for analyzing household survey data, providing insights into income distribution, poverty levels, and Medicaid eligibility.

