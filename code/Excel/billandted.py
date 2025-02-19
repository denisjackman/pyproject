#!/usr/bin/env python
'''
    bill and ted python
'''
import openpyxl


def main():
    ''' main function '''
    workbook = openpyxl.load_workbook(filename="Z:/Resources/excel/hello.xlsx")

    # The workbook object is then used to add new
    # worksheet via the add_worksheet() method.
    worksheet = workbook.create_sheet("test2")

    # Use the worksheet object to write
    # data via the write() method.
    worksheet['A1'] = 'Hello.. Again'
    worksheet['B1'] = 'Freaks'
    worksheet['C1'] = 'For'
    worksheet['D1'] = 'Geeks'
    worksheet['E1'] = 'WooooWooooo'
    workbook.save('Z:/Resources/excel/hello2.xlsx')


if __name__ == '__main__':
    main()
