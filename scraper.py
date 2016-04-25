from lxml import html
import requests
from bs4 import BeautifulSoup

def scraper(url,visited = None,depth = 0):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36'}

    visited = set() if visited == None else visited
    if depth >= 1:
        return visited
    else:
        raw = requests.get(url,headers=headers)
        encoding = raw.encoding
        decoded = raw.content.decode(encoding)
        soup = BeautifulSoup(decoded,"lxml")
        if url not in visited and url.startswith("http"):
            visited.add(url)
        for link in soup.find_all('a'):
            href = link.get('href')
            if (type(href)==str and href not in visited
                                        # and href.startswith("http")):
                                    and  href.startswith("/wiki/")):
                href = "https://en.wikipedia.org" + href
                visited.add(href)
                print("    "*depth,href)
                try:
                    visited = scraper(href,visited,depth+1)
                except:
                    continue
        return visited


url = "https://en.wikipedia.org/wiki/Resource"
result = scraper(url)
print("-------")
for link in result:
    pass






