import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#URLの指定
html = urlopen("http://npb.jp/teams/")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.findAll("div", {"class": "team_unit"})

for teams in table:
    # テーブルを指定
    rows = teams.findAll("tr")
    team_name = teams.findAll("dt")
    print(team_name[0].get_text())

    with open(team_name[0].get_text() + "_npb.csv", 'wt', newline='', encoding='utf-8') as f:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            csv.writer(f).writerow(csvRow)

