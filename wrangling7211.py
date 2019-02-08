from csv import DictReader

data_rdr = DictReader(open('../data-wrangling/data/unicef/mn.csv', 'rt'))
header_rdr = DictReader(open('../data-wrangling/data/unicef/mn_headers.csv', 'rt'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr]

print(data_rows[:5])
print(header_rows[:5])

new_rows = []
for data_dict in data_rows:
	new_row = {}
	for dkey, dval in data_dict.items():
		for header_dict in header_rows:
			if dkey in header_dict.values():
				new_row[header_dict.get('Label')] = dval
	new_rows.append(new_row)
				
print(new_rows[0])

'''
for data_dict in data_rows:
	for dkey, dval in data_dict.items():
		for header_dict in header_rows:
			for hkey, hval in header_dict.items():
				if dkey == hval:
					print('match!')
'''