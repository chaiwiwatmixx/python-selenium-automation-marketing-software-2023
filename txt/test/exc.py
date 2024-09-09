import xlsxwriter
import os
import sys
from os import path

Fullpath = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))

print(Fullpath)
print(type(Fullpath))

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(f'{Fullpath}\\Expenses01.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000, 1],
    ['Gas',   100, 2],
    ['Food',  300, 3],
    ['Gym',    50, 4],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost, i in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    worksheet.write(row, col + 2, i)
    row += 1

# Write a total using a formula.
# worksheet.write(row, 0, 'Total')
# worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()