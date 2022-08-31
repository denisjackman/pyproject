#!/usr/bin/env python
'''
    bill and ted python
'''
# import xlsxwriter module
import openpyxl
# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.

workbook = openpyxl.load_workbook(filename="Y:/Resources/store/hello.xlsx")

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
sheet = workbook.active
worksheet = workbook.create_sheet("test2")

# Use the worksheet object to write
# data via the write() method.
worksheet['A1'] = 'Hello.. Again'
worksheet['B1'] = 'Freaks'
worksheet['C1'] = 'For'
worksheet['D1'] = 'Geeks'
worksheet['E1'] = 'WooooWooooo'
workbook.save('Y:/Resources/store/hello2.xlsx')
