from urllib.request import urlopen
from bs4 import BeautifulSoup

#URLの指定
html = urlopen("https://www.amazon.co.jp/gp/bestsellers/digital-text/2292561051/ref=pd_zg_hrsr_digital-text_1_4_last")
bsObj = BeautifulSoup(html, "html.parser")

#テーブルを指定
toplinks = bsObj.findAll("div", {"class": "zg_item_compact"})
rows = toplinks[0].findAll("a", {"class": "a-link-normal"})[0]
# print(rows)
# print(rows.get("href"))
amazon = "https://www.amazon.co.jp/"

# html_review = urlopen(amazon + rows.get("href"))
# reviewObj = BeautifulSoup(html_review, "html.parser")

html_review = urlopen(amazon + "%E3%81%A9%E3%82%93%E3%81%A9%E3%82%93%E8%A9%B1%E3%81%99%E3%81%9F%E3%82%81%E3%81%AE%E7%9E%AC%E9%96%93%E8%8B%B1%E4%BD%9C%E6%96%87%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%EF%BC%88CD%E3%81%AA%E3%81%97%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%EF%BC%89-%E6%A3%AE%E6%B2%A2%E6%B4%8B%E4%BB%8B-ebook/product-reviews/B00UCUNAKU/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1")
reviewObj = BeautifulSoup(html_review, "html.parser")
reviews = reviewObj.findAll("span", {"class": "review-text"})
votes = reviewObj.findAll("span", {"class": "cr-vote-text"})
print(reviews[0].get_text())
print(votes[0].get_text()[0:2], "人のお客様がこれが役に立ったと考えています")
