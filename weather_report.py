import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#URLの指定
html = urlopen("https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2018&month=9")
bsObj = BeautifulSoup(html, "html.parser")

#テーブルを指定
table = bsObj.findAll("table", {"class": "data2_s"})[0]
rows = table.findAll("tr")

csvFile = open("weather.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
