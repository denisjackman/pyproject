'''
a contining series of xl tutorials
'''
from openpyxl import load_workbook


def main():
    ''' main function '''
    wb = load_workbook('y:/Resources/excel/tim.xlsx')
    ws = wb.active
    # insert and delete rows
    ws.insert_rows(7)
    ws.delete_rows(7)

    # insert and delete columns
    ws.insert_cols(2)
    ws.delete_cols(2)

    # move a range
    ws.move_range("C1:D11", rows=2, cols=2)

    wb.save('y:/Resources/excel/tim3.xlsx')


if __name__ == '__main__':
    main()
