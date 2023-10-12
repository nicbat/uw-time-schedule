import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.washington.edu/students/timeschd/AUT2023/chem.html")
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
        obj = {}
        # print(children)
        try:
            if children[1].split()[2] == "to":
                continue
            # TODO Hybrid lectures have multiple listings for times that they happen
            obj["sln"] = int(children[0])
            obj["letter"] = children[1].split()[0]
            obj["credits"] = (children[1].split()[1])
            obj["days"] = children[1].split()[2]
            obj["times"] = children[1].split()[3]
            obj["building"] = children[2]
            obj["room"] = children[3].split()[0]
        except:
            print("error on", children)
            # exit
        current[-1]["classes"].append(obj)
    else:
        current.append({"name": " ".join(children[0].split()), "classes":[]})
for c in current:
    print(c["name"], [d["sln"] for d in c["classes"]])