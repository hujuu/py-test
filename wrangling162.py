from csv import reader

data_rdr = reader(open('../data-wrangling/data/unicef/mn.csv', 'rt'))
header_rdr = reader(open('../data-wrangling/data/unicef/mn_headers.csv', 'rt'))

data_rows = [d for d in data_rdr]

header_rows = [h for h in header_rdr if h[0] in data_rows[0]]

print(len(header_rows))

all_short_headers = [h[0] for h in header_rows]

skip_index = []

for header in data_rows[0]:
	if header not in all_short_headers:
		index = data_rows[0].index(header)
		skip_index.append(index)

new_data = []

for row in data_rows[1:]:
	new_row = []
	
	for i, d in enumerate(row):
		if i not in skip_index:
			new_row.append(d)
	new_data.append(new_row)

zipped_data = []

for drow in new_data:
	zipped_data.append(zip(header_rows, drow))
	
print(list(zipped_data[0]))


data_headers = []
for i, header in enumerate(data_rows[0]):
	if i not in skip_index:
		data_headers.append(header)
		
header_match = zip(data_headers, all_short_headers)

print(list(header_match))