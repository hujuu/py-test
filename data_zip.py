from csv import reader

data_rdr = reader(open('../data-wrangling/data/unicef/mn.csv', 'rt'))
header_rdr = reader(open('../data-wrangling/data/unicef/mn_headers_updated.csv', 'rt'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]

print (len(header_rows))

all_short_headers = [h[0] for h in header_rows]

skip_index = []
final_header_rows = []

for header in data_rows[0]:
	if header not in all_short_headers:
		index = data_rows[0].index(header)
		skip_index.append(index)
	else:
		for head in header_rows:
			if head[0] == header:
				final_header_rows.append(head)
				break

#del all_short_headers
new_data = []

for row in data_rows[1:]:
	new_row = []
	for i, d in enumerate(row):
		if i not in skip_index:
			new_row.append(d)
	new_data.append(new_row)

zipped_data = []

for drow in new_data:
	zipped_data.append(list(zip(header_rows, drow)))

print (zipped_data[0])

data_headers = []

for i, header in enumerate(data_rows[0]):
	if i not in skip_index:
		data_headers.append(header)
		
header_match = zip(data_headers, all_short_headers)
#print(list(header_match))

for x in zipped_data[0]:
	print('Qustion: {[1]}\nAnswer: {}'.format(x[0], x[1]))
	
for x in enumerate(zipped_data[0][:20]):
	print(x)
	
from datetime import datetime

start_string = '{}/{}/{} {}:{}'.format(
	zipped_data[0][8][1], zipped_data[0][7][1], zipped_data[0][9][1],
	zipped_data[0][13][1], zipped_data[0][14][1]
)

print(start_string)

start_time = datetime.strptime(start_string, '%m/%d/%Y %H:%M')

print(start_time)

end_time = datetime(
	int(zipped_data[0][9][1]), int(zipped_data[0][8][1]),
	int(zipped_data[0][7][1]), int(zipped_data[0][15][1]),
	int(zipped_data[0][16][1])
)

print(end_time)

duration = end_time - start_time

print(duration)
print(duration.days)
print(duration.total_seconds())

minutes = duration.total_seconds() / 60.0

print(minutes)

print(end_time.strftime('%m/%d/%Y %H:%M'))

print(start_time.ctime())

print(start_time.strftime('%Y-%m-%dT%H:%M:%S'))

for answer in zipped_data[0]:
	if not answer[1]:
		print(answer)
		
for row in zipped_data:
	for answer in row:
		if answer[1] is None:
			print(answer)