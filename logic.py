from requests_html import HTMLSession
from bs4 import BeautifulSoup


class ParseUrl:
    def __init__(self, url):

        # Get the page content
        self.titles = dict()
        self.index = 0
        self.session = HTMLSession()
        self.page = self.session.get(url)
        self.parse_to_bs = BeautifulSoup(self.page.content, "html.parser")
        self.links = self.parse_to_bs.find_all("a")

        # Parse the values into a
        for link in self.links:
            content = link.findChildren("h3", text=True)
            if len(content) > 0 and len(self.titles) < 3 and len(link.get("href")) < 100:
                self.titles.update({content[0].getText().upper(): "http://reddit.com/" + link.get("href")})

