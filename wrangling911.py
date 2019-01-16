import xlrd
import agate

workbook = xlrd.open_workbook('unicef_oct_2014.xls')
print(workbook.nsheets)
print(workbook.sheet_names())

sheet = workbook.sheets()[0]
sheet.nrows # ❶
sheet.row_values(0) # ❷
for r in range(sheet.nrows):
	print(r, sheet.row(r)) # ❸
	
title_rows = list(zip(sheet.row_values(4), sheet.row_values(5)))
print(title_rows)

titles = [t[0] + ' ' + t[1] for t in title_rows]
print(titles)
titles = [t.strip() for t in titles]

country_rows = [sheet.row_values(r) for r in range(6, 114)]

from xlrd.sheet import ctype_text
import agate
text_type = agate.Text()
number_type = agate.Number()
boolean_type = agate.Boolean()
date_type = agate.Date()
example_row = sheet.row(6)
print(example_row) # ❶
print(example_row[0].ctype) # ❷
print(example_row[0].value)
print(ctype_text) # ❸