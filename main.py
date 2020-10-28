from requests_html import HTMLSession as request
from bs4 import BeautifulSoup


def parse_url(url):
    session = request()
    page = session.get(url)
    parse_to_bs = BeautifulSoup(page.content, "html.parser")
    links = parse_to_bs.find_all("a")
    for link in links:
        content = link.findChildren("h3", text=True)
        if len(content) > 0:
            print(content[0].getText())
            print("http://reddit.com/" + link.get("href"))
            print("\n")


if __name__ == '__main__':
    parse_url("https://www.reddit.com/r/news")
