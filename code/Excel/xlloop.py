'''
a contining series of xl tutorials
'''
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook('tim.xlsx')
ws = wb.active
for xlrow in range(1, 11):
    for xlcol in range(1, 5):
        # char - chr(65 + xlcol)
        char = get_column_letter(xlcol)
        print(ws[char + str(xlrow)].value)
        ws[char + str(xlrow)] = char + str(xlrow)

ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
ws.append(['end'])


wb.save('tim.xlsx')
