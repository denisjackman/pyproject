'''
a contining series of xl tutorials
'''
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'Data'

ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
ws.append(['end'])


wb.save('tim.xlsx')
