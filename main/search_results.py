from bs4 import BeautifulSoup
from requests import get

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}


def results_data(keywords="movies"):
    final_data = []

    try:

        url = f"https://www.google.com/search?q=site%3Adrive.google.com+{keywords}"
        page = get(url, headers=headers)

        page_contents = BeautifulSoup(page.content, "html.parser")
        data_parent = page_contents.find("div", {"id": "search"})

        data_containers = data_parent.findAll("div", class_="yuRUbf")

        if len(data_containers) == 0:
            return False
        
        else:
            id = 0
            for container in data_containers:
                data_dict = {
                    "id": id,
                    "title": (container.h3.string),
                    "link": (container.a["href"]),
                    "path": (container.span.string)
                }
                final_data.append(data_dict)
                id += 1

            return final_data

    except:
        return 0



