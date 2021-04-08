from bs4 import BeautifulSoup
from urllib.request import urlopen


def create_comment(comment_soup):
    children = []
    try:
        for child in comment_soup.find("div", class_="comments__item__children").find_all("div", class_="comments__item"):
            children.append(create_comment(child))
    except TypeError or AttributeError:
        pass
    children_comments = {
        "author": comment_soup.find("p", class_="comments__item__user__name").get_text(),
        "text": comment_soup.find("div", class_="comments__item__text").get_text(),
        "child_comments": children
    }
    return children_comments


url = "https://dtf.ru/games/696984-gruppa-zashchity-musulman-prizyvaet-valve-zapretit-prodazhu-igry-six-days-in-fallujah"
page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
comments_soup = [tag for tag in soup.find_all("div", {"class": "comments__item"})]
comments = [create_comment(comment) for comment in comments_soup]

for item in comments:
    print(item)
