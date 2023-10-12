import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.washington.edu/students/timeschd/AUT2023/cse.html")
soup = BeautifulSoup(r.content, features="html.parser")

# print(soup)
classes = []

tables = soup.body.find_all('table')
del tables[0:3]
current = []
for table in tables:
    children = [child.string for child in table.descendants if child.name == None]
    children.pop(0)
    if 'pre' in [child.name for child in table.descendants]:
        links = table.find_all("a")
        if len(links) == 1:
            continue
        obj = {}
        if children[1].split()[2] == "to":
            continue
        obj["sln"] = int(links[0].contents[0])
        links.pop(0)
        obj["letter"] = children[1].split()[0]
        obj["credits"] = (children[1].split()[1])
        obj["locations"] = [{"days": children[1].split()[2], "time": children[1].split()[3], "building": links[0].contents[0], "room": children[3].split()[0]}]
        links.pop(0)
        additional = 0
        while len(links) > 0:
            times = children[3 + (2*additional)].split("\n")[1].split()
            extra = {}
            extra["days"] = times[0]
            extra["time"] = times[1]
            extra["building"] = links[0].contents[0]
            extra["room"] = children[5 + (2*additional)].split()[0]
            obj["locations"].append(extra)
            links.pop(0)
        current[-1]["classes"].append(obj)
    else:
        current.append({"name": " ".join(children[0].split()), "classes":[]})
for c in current:
    print(c["name"], [d for d in c["classes"]])