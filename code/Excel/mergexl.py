'''
a contining series of xl tutorials
'''
import sys
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook('tim.xlsx')
ws = wb.active

ws.merge_cells('A1:E1')
ws.merge_cells('A2:E2')

ws.unmerge_cells('A1:E1')

wb.save('tim.xlsx')