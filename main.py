from bs4 import BeautifulSoup
from urllib.request import urlopen


def create_comment(comment_soup):
    children_comments = []
    for comment in comment_soup.find("div", class_="comments__item"):
        try:
            children_comments.append({
                "author": comment.find("p", class_="comments__item__user__name").get_text(),
                "text": comment.find("div", class_="comments__item__text").get_text(),
                "child_comments": create_comment(comment.find("div", class_="comments__item_children"))
            })
        except AttributeError:
            children_comments.append({
                "author": comment.find("p", class_="comments__item__user__name").get_text(),
                "text": comment.find("div", class_="comments__item__text").get_text(),
            })
    return children_comments


url = "https://dtf.ru/games/693406-ya-vnimatelno-slushal-no-malo-chto-ponyal-edzi-sinkava-rasskazal-o-rabote-nad-death-stranding?comment=10016724"
page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
comments_soup = [tag for tag in soup.find_all("div", {"class": "comments__item"})]
comments = []
for comment in comments_soup:
    try:
        comments.append({
            "author": comment.find("p", class_="comments__item__user__name").get_text(),
            "text": comment.find("div", class_="comments__item__text").get_text(),
            "child_comments": create_comment(comment.find("div", class_="comments__item_children"))
        })
    except AttributeError:
        comments.append({
            "author": comment.find("p", class_="comments__item__user__name").get_text(),
            "text": comment.find("div", class_="comments__item__text").get_text(),
        })

for item in comments:
    print(item)
