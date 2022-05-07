from tkinter.tix import Tree
from bs4 import BeautifulSoup
from requests import get

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}


def results_data(keywords="movies"):
    final_data = []

    try:

        url = f"https://www.google.com/search?q=site%3Adrive.google.com+{keywords}"
        page = get(url, headers=headers)

        page_contents = BeautifulSoup(page.content, "lxml")
        data_parent = page_contents.find("div", {"id": "search"})

        data_containers = data_parent.findAll("div", class_="yuRUbf")

        if len(data_containers) == 0:
            return False
        
        else:
            id = 0
            # folder = False
            for container in data_containers:
                drive_link = (container.a["href"])
                # folder_check = drive_link.replace("https://drive.google.com/drive/", "")
                # if folder_check[0] == "f":
                #     folder = True

                # folder = True if folder_check[0] == "f" else False
                data_dict = {
                    "id": id,
                    "title": (container.h3.string),
                    "link": drive_link,
                    "path": (container.span.string),
                    # "folder": folder
                }
                final_data.append(data_dict)
                id += 1

            return final_data

    except:
        return 0



