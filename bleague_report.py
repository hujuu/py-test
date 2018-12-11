import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#URLの指定
html = urlopen("https://www.bleague.jp/standings/?tab=1&year=2017")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.findAll("div", {"class": "modal-wrap"})

for teams in table:
    # テーブルを指定
    rows = teams.findAll("tr")
    team_name = teams.findAll("h4")
    print(team_name[0].get_text())

    with open(team_name[0].get_text() + "_bleague.csv", 'wt', newline='', encoding='utf-8') as f:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            csv.writer(f).writerow(csvRow)

