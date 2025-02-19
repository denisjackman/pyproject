'''
a contining series of xl tutorials
'''
from openpyxl import Workbook


def main():
    ''' main function '''
    wb = Workbook()
    ws = wb.active
    ws.title = 'Data'
    ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
    ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
    ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
    ws.append(['Tim', 'Is', 'Great', 'Always', '!'])
    ws.append(['end'])
    wb.save('y:/Resources/excel/tim5.xlsx')


if __name__ == '__main__':
    main()
