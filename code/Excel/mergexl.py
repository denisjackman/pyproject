'''
a contining series of xl tutorials
'''
from openpyxl import load_workbook

wb = load_workbook('tim.xlsx')
ws = wb.active

ws.merge_cells('A1:E1')
ws.merge_cells('A2:E2')

ws.unmerge_cells('A1:E1')

wb.save('tim.xlsx')