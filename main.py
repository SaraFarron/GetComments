from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://dtf.ru/games/693406-ya-vnimatelno-slushal-no-malo-chto-ponyal-edzi-sinkava-rasskazal-o-rabote-nad-death-stranding?comment=10016724"
page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
res = [tag for tag in soup.find_all("div", {"class": "comments__item__content"})]
print(res[0].findChildren())