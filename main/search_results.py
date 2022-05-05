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
        id = 0
        for x in data_containers:
            data_dict = {
                "id": id,
                "title": x.h3,
                "link": (x.a["href"])
            }

            final_data.append(data_dict)

            # print("-"*40)
            # print((x.h3).text)
            # y = x.a
            id += 1
            # print(y["href"])
        return final_data

    except:
        pass


results_data("india")
