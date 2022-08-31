'''
 Reading an excel file using Python
'''
import openpyxl

# Give the location of the file
loc = openpyxl.load_workbook("y:/Resources/store/test.xlsx")

sheet = loc.active

# For row 2 and column 1
print (sheet.cell(row=2, column=1).value)
print (sheet.cell(row=3, column=1).value)
print (sheet.cell(row=4, column=1).value)
