import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.washington.edu/students/timeschd/AUT2023/")
soup = BeautifulSoup(r.content, features="html.parser")

lists = soup.body.find_all('div', class_="container uw-body")[0].find_all('li')

thing = lists[0].contents[0].attrs["href"]
links = [li.contents[0].attrs["href"] for li in lists if li.contents[0].name == 'a' and "title" not in li.contents[0].attrs.keys() and "href" in li.contents[0].attrs.keys()]
# print(len(links))
# for link in links:
#     print(link)
print(links)