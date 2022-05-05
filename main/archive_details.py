from tempfile import tempdir
from bs4 import BeautifulSoup
from requests import get

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}


def results_data():
    final_data = []

    try:
        url = "https://drive.google.com/drive/mobile/folders/0BzL6M5WpOxAdTTJRaW4yZFhMeTQ/0BzL6M5WpOxAdUW1ON2RwWS1YZk0?sort=13&direction=a"
        # url = f"https://www.google.com/search?q=site%3Adrive.google.com+{keywords}"
        page = get(url, headers=headers)

        page_contents = BeautifulSoup(page.content, "html.parser")
        # data_parent = page_contents.find("div", {"class" : "VIrDCd"})
        data_parent = page_contents.find("div", {"class" : "pdAMZe"})

        data_containers = data_parent.findAll("div", {"jsname": "LvFR7c"})
        # data_containers = data_parent.findAll("div", {"jscontroller": "LPQUTd"})
        
        for container in data_containers:
            print("-" * 40) 
            temp = container.find("div" , {"class", "Q5txwe"})
            print(temp)
            # print(container)
        print(len(data_containers))
      
    except:
        print("error occurred")

results_data()
