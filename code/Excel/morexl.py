'''
a contining series of xl tutorials
'''

from openpyxl import load_workbook

wb = load_workbook('tim.xlsx')
ws = wb.active
# insert and delete rows
ws.insert_rows(7)
ws.delete_rows(7)

# insert and delete columns
ws.insert_cols(2)
ws.delete_cols(2)

# move a range
ws.move_range("C1:D11", rows=2, cols=2)

wb.save('tim.xlsx')
