from django.test import TestCase

# Create your tests here.
from bs4 import BeautifulSoup
import requests


def parse_article(item):
    result = {"title": item.h3.contents[0], "content_link": item.a.attrs["href"], "before": item.a.b.contents[0]}
    return result


def get_content(content_link):
    content = requests.get(content_link).content.decode("UTF-8")
    soup = BeautifulSoup(content)
    span = soup.find("div", {"id": "story_body_content"}).find_all("p")
    result = []
    for s in span:
        result += [i for i in s.contents if isinstance(i,str)]
    return "".join(result)

if __name__ == "__main__":
    root = "https://nba.udn.com/nba/index"
    text = requests.get("https://nba.udn.com/nba/index?gr=www").content.decode("UTF-8")
    soup = BeautifulSoup(text)
    all_news = soup.find("div", {"id": "news_body"}).find_all("dt")
    for n in all_news:
        if 'ads' not in n.attrs.get('class', []):
            item = parse_article(n)
            content = get_content(f"https://nba.udn.com{item['content_link']}")
            print(content)
            print()
